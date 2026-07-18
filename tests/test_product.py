import unittest
import json
from pathlib import Path

import product
from runtime.server import page, result_markup


class ProductTests(unittest.TestCase):
    def test_fixed_acceptance(self):
        result = product.analyze({field.name: field.value for field in product.PRODUCT.fields})
        passed, checks = product.acceptance(result)
        self.assertTrue(passed, checks)

    def test_page_is_product_specific_and_escapes_output(self):
        self.assertIn(product.PRODUCT.name, page())
        self.assertNotIn("<script>", result_markup({"status": "<script>", "headline": "safe", "metrics": {}, "items": [], "evidence": [], "artifact": {}}))

    def test_public_fixture_matches_engine_fixture(self):
        site = Path("site/app/product-data.ts").read_text()
        result = product.analyze({field.name: field.value for field in product.PRODUCT.fields})
        for decision in json.loads(product.DECISIONS):
            self.assertIn(f'"id":"{decision["id"]}"', site)
            self.assertIn(f'"decision":"{decision["decision"]}"', site)
            self.assertIn(decision["invalidate_when"], site)
            self.assertIn(decision["review_when"], site)
        for decision_id, evidence in json.loads(product.EVIDENCE).items():
            self.assertIn(f'"{decision_id}"', site)
            self.assertIn(evidence["source"], site)
        self.assertIn(result["status"], site)
        for title in ("D-1 is invalidated", "D-2 remains valid", "D-3 is at risk"):
            self.assertIn(title, site)

    def test_new_evidence_can_restore_current_status(self):
        evidence = json.loads(product.EVIDENCE)
        evidence["D-1"]["quality"] = 85
        evidence["D-3"]["complaints"] = 2
        result = product.analyze({"decisions": product.DECISIONS, "evidence": json.dumps(evidence)})
        self.assertEqual(result["status"], "CURRENT")
        self.assertEqual(result["metrics"], {"valid": 3, "at_risk": 0, "invalidated": 0})


if __name__ == "__main__":
    unittest.main()
