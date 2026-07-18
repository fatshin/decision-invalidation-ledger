from __future__ import annotations

import json
import operator
import re
from typing import Any

from runtime.contracts import Field, Product


DECISIONS = json.dumps([
    {"id": "D-1", "decision": "Use Model A", "invalidate_when": "quality < 80", "review_when": "cost > 200000"},
    {"id": "D-2", "decision": "Keep vendor B", "invalidate_when": "uptime < 99.5", "review_when": "incidents > 2"},
    {"id": "D-3", "decision": "Launch workflow C", "invalidate_when": "completion < 90", "review_when": "complaints > 5"},
], indent=2)
EVIDENCE = json.dumps({
    "D-1": {"quality": 77, "cost": 180000, "source": "eval-2026-07-18.csv"},
    "D-2": {"uptime": 99.8, "incidents": 1, "source": "status-q2.json"},
    "D-3": {"completion": 93, "complaints": 7, "source": "launch-week.csv"},
}, indent=2)
OPS = {"<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge, "==": operator.eq}

PRODUCT = Product(
    5, "decision-invalidation-ledger", "Decision Invalidation Ledger",
    "Make assumptions executable so new evidence can reopen yesterday’s decisions.",
    "#14b8a6",
    (Field("decisions", "Decision ledger (JSON)", DECISIONS, 14), Field("evidence", "New evidence (JSON)", EVIDENCE, 14)),
)


def condition_result(condition: str, values: dict[str, Any]) -> tuple[bool, str]:
    match = re.fullmatch(r"\s*([a-z_]+)\s*(<=|>=|==|<|>)\s*([\d.]+)\s*", condition)
    if not match:
        raise ValueError(f"Unsupported condition: {condition}")
    key, symbol, threshold = match.groups()
    if key not in values:
        return False, f"Missing evidence for {key}"
    actual, expected = float(values[key]), float(threshold)
    return OPS[symbol](actual, expected), f"{key}={actual:g} {symbol} {expected:g}"


def assess(decision: dict[str, str], evidence: dict[str, Any]) -> dict[str, Any]:
    invalid, invalid_trace = condition_result(decision["invalidate_when"], evidence)
    review, review_trace = condition_result(decision["review_when"], evidence)
    return {"id": decision["id"], "decision": decision["decision"], "status": "INVALIDATED" if invalid else "AT_RISK" if review else "VALID", "evidence": invalid_trace if invalid else review_trace, "source": evidence.get("source", "unknown")}


def analyze(payload: dict[str, str]) -> dict[str, Any]:
    decisions, evidence = json.loads(payload["decisions"]), json.loads(payload["evidence"])
    items = [assess(item, evidence.get(item["id"], {})) for item in decisions]
    invalid = sum(item["status"] == "INVALIDATED" for item in items)
    return {
        "status": "ACTION_REQUIRED" if invalid else "CURRENT",
        "headline": f"{invalid} decision invalidated by new evidence",
        "metrics": {state.lower(): sum(item["status"] == state for item in items) for state in ("VALID", "AT_RISK", "INVALIDATED")},
        "items": items,
        "evidence": [{"label": key, "value": value["source"]} for key, value in evidence.items()],
        "artifact": {"ledger_version": "1", "assessments": items},
    }


def acceptance(result: dict[str, Any]) -> tuple[bool, dict[str, bool]]:
    checks = {"three_decisions": len(result["items"]) == 3, "state_distribution": result["metrics"] == {"valid": 1, "at_risk": 1, "invalidated": 1}, "source_links": all(item["source"] != "unknown" for item in result["items"])}
    return all(checks.values()), checks

