# Decision Invalidation Ledger — Submission

**Tagline:** Detect when new evidence invalidates an old decision.

**Category:** Work & Productivity  
**Codex Session ID:** `019f7306-7262-7371-a03f-6b99df7129bf`

## What it does

The ledger records a decision with its assumptions and review triggers. New
evidence is matched against those assumptions to classify the decision as
valid, at risk, or invalidated.

## How it was built

I used Codex with GPT-5.6 to implement the ledger schema, trigger comparison,
three-state evaluation, tests, and browser interface. A future live path can use
GPT-5.6 to extract candidate assumptions; the public demo uses a tested fixture,
and owners approve the final assumptions and triggers.

## Proof

- one valid, one at-risk, and one invalidated decision
- every status links to an assumption and new evidence
- deterministic fixture and narrated demo

## Links

- Live product: https://decision-invalidation-ledger.fatshin.chatgpt.site
- Source: https://github.com/fatshin/decision-invalidation-ledger
- Devpost draft: https://devpost.com/software/decision-invalidation-ledger
- Video: `UPLOAD_TO_YOUTUBE_AND_REPLACE`

## Limits

Real deployments require named owners and durable evidence sources.
