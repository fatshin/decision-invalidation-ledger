import type { Product } from "./product-types";

export const product: Product = {
  number: "05",
  name: "Decision Invalidation Ledger",
  eyebrow: "Decisions that know when they expire",
  tagline: "Detect when new evidence invalidates an old decision.",
  description: "Record decisions with the assumptions that support them, then compare new evidence and show which decisions remain valid, are at risk, or must be reopened.",
  accent: "#8c5cff",
  inputLabel: "Decision ledger update",
  inputHint: "The same three decisions and evidence records are evaluated by product.py.",
  inputValue: "D-1 Use Model A: invalidate quality <80; observed 77.\nD-2 Keep vendor B: invalidate uptime <99.5; observed 99.8.\nD-3 Launch workflow C: review complaints >5; observed 7.",
  actionLabel: "Reveal verified result",
  status: "ACTION_REQUIRED",
  statusTone: "warn",
  metrics: [{ value: "1", label: "valid" }, { value: "1", label: "at risk" }, { value: "1", label: "invalidated" }],
  findings: [
    { title: "D-1 is invalidated", detail: "quality=77 is below the explicit floor of 80.", badge: "INVALIDATED", tone: "bad" },
    { title: "D-2 remains valid", detail: "uptime=99.8 remains above the 99.5 invalidation boundary.", badge: "VALID", tone: "good" },
    { title: "D-3 is at risk", detail: "complaints=7 crosses the review trigger of 5.", badge: "AT RISK", tone: "warn" },
  ],
  method: [
    { step: "01", title: "Register", detail: "Store the decision, owner, assumptions, evidence, and review trigger." },
    { step: "02", title: "Compare", detail: "Match new facts to the assumptions they can weaken or replace." },
    { step: "03", title: "Reopen", detail: "Notify the owner with the exact evidence that crossed the trigger." },
  ],
  proof: ["Explicit assumptions", "Three-state outcome", "Evidence-linked reopen"],
  note: "The ledger fixture is synthetic. Real decisions require named owners and durable evidence sources.",
};
