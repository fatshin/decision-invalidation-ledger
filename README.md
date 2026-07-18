# Decision Invalidation Ledger

Decision Invalidation Ledger stores a decision beside the evidence conditions
that would reopen it. New evidence changes each item to `VALID`, `AT_RISK`, or
`INVALIDATED` without rewriting the original decision.

## Judge path

1. Run `./scripts/run.sh --port 8105`.
2. Open `http://127.0.0.1:8105`.
3. Select **Run analysis**.
4. Confirm one decision in each state.
5. Expand the invalidated decision and follow its value, threshold, and source.

## What is implemented

- three-decision JSON ledger;
- small auditable condition DSL;
- invalidation-before-review precedence;
- source-linked status evidence;
- machine-readable assessment timeline.

## Verification

```sh
./scripts/check.sh
```

## OpenAI and Codex

Codex was used for implementation and validation. GPT-5.6 can extract candidate
assumptions and conditions from decision documents, but humans approve the
ledger and the deterministic evaluator owns status changes.

## Limits

The DSL supports numeric comparisons only. The MVP does not fetch external
evidence or change operational systems when a decision becomes invalid.

