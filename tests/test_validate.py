import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", ROOT / "scripts" / "validate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PlanValidation(unittest.TestCase):
    def sample(self):
        return json.loads((ROOT / "examples" / "research-notes.json").read_text(encoding="utf-8"))

    def test_synthetic_example_is_valid(self):
        self.assertEqual(module.validate(self.sample()), [])

    def test_domain_constraint_is_enforced(self):
        bad = self.sample()
        bad['birth_data_collected'] = True
        self.assertTrue(module.validate(bad))

    def test_conflicting_work_plan_is_rejected(self):
        bad = self.sample()
        bad['notes'][0]['claim_type'] = 'clinical_diagnosis'
        self.assertTrue(module.validate(bad))

    def test_private_record_is_not_a_public_example(self):
        bad = self.sample()
        bad['data_classification'] = 'private'
        self.assertTrue(module.validate(bad))

    def test_non_object_is_rejected(self):
        self.assertTrue(module.validate([]))
