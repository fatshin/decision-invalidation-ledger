import type { Product } from "./product-types";

export const product: Product = {
  number: "05",
  name: "Decision Invalidation Ledger",
  eyebrow: "Decisions that know when they expire",
  tagline: "Detect when new evidence invalidates an old decision.",
  description: "Record decisions with the assumptions that support them, then compare new evidence and show which decisions remain valid, are at risk, or must be reopened.",
  accent: "#8c5cff",
  inputLabel: "Decision ledger update",
  inputHint: "Three decisions are checked against a new evidence packet.",
  inputValue: "D-101 assumes vendor uptime ≥99.9%. D-102 assumes launch demand ≤10k users. D-103 assumes regulation R-4 remains unchanged. New evidence: uptime 99.93%; forecast 9.8k–12.4k; R-4 was replaced yesterday.",
  actionLabel: "Check invalidations",
  status: "ACTION_REQUIRED",
  statusTone: "warn",
  metrics: [{ value: "1", label: "valid" }, { value: "1", label: "at risk" }, { value: "1", label: "invalidated" }],
  findings: [
    { title: "D-101 remains valid", detail: "Measured uptime still satisfies the explicit 99.9% assumption.", badge: "VALID", tone: "good" },
    { title: "D-102 is at risk", detail: "The forecast range crosses the assumed capacity even though its midpoint does not.", badge: "AT RISK", tone: "warn" },
    { title: "D-103 is invalidated", detail: "The governing regulation changed, so the decision must be reopened.", badge: "INVALIDATED", tone: "bad" },
  ],
  method: [
    { step: "01", title: "Register", detail: "Store the decision, owner, assumptions, evidence, and review trigger." },
    { step: "02", title: "Compare", detail: "Match new facts to the assumptions they can weaken or replace." },
    { step: "03", title: "Reopen", detail: "Notify the owner with the exact evidence that crossed the trigger." },
  ],
  proof: ["Explicit assumptions", "Three-state outcome", "Evidence-linked reopen"],
  note: "The ledger fixture is synthetic. Real decisions require named owners and durable evidence sources.",
};
