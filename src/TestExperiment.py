import unittest
from Experiment import Experiment
from SignalDetection import SignalDetection

class TestExperiment(unittest.TestCase):
    
    # Test: add_condition() stores SignalDetection objects correctly
    def test_add_condition(self):
        exp = Experiment()
        sdt = SignalDetection(20, 10, 15, 5)
        exp.add_condition(sdt, label="Condition A")

        self.assertEqual(len(exp.conditions), 1)
        self.assertEqual(exp.conditions[0], sdt)
        self.assertEqual(exp.labels[0], "Condition A")

    # Test: add_condition() raises error for invalid input
    def test_add_condition_invalid_type(self):
        exp = Experiment()
        with self.assertRaises(TypeError):
            exp.add_condition("Invalid Object", label="Condition B")

    # Test: sorted_roc_points() returns sorted values
    def test_sorted_roc_points(self):
        exp = Experiment()
        exp.add_condition(SignalDetection(30, 10, 20, 10), label="A")
        exp.add_condition(SignalDetection(50, 5, 10, 35), label="B")

        fa_rates, h_rates = exp.sorted_roc_points()

        # Ensure false alarm rates are sorted in ascending order
        self.assertTrue(all(x <= y for x, y in zip(fa_rates, fa_rates[1:])))

    # Test: sorted_roc_points() raises an error for empty experiment
    def test_sorted_roc_points_empty(self):
        exp = Experiment()
        with self.assertRaises(ValueError):
            exp.sorted_roc_points()

    # Test: compute_auc() returns 0.5 for (0,0) → (1,1)
    def test_compute_auc_half(self):
        exp = Experiment()
        exp.add_condition(SignalDetection(0, 0, 0, 100), label="(0,0)")
        exp.add_condition(SignalDetection(100, 0, 100, 0), label="(1,1)")

        self.assertAlmostEqual(exp.compute_auc(), 0.5, places=2)

    # Test: compute_auc() returns 1.0 for (0,0) → (0,1) → (1,1)
    def test_compute_auc_one(self):
        exp = Experiment()
        exp.add_condition(SignalDetection(0, 0, 0, 100), label="(0,0)")
        exp.add_condition(SignalDetection(100, 0, 0, 100), label="(0,1)")
        exp.add_condition(SignalDetection(100, 0, 100, 0), label="(1,1)")

        self.assertAlmostEqual(exp.compute_auc(), 1.0, places=2)

    # Test: compute_auc() raises error for empty experiment
    def test_compute_auc_empty(self):
        exp = Experiment()
        with self.assertRaises(ValueError):
            exp.compute_auc()

    # Test: compute_auc() for a general case
    def test_compute_auc_random(self):
        exp = Experiment()
        exp.add_condition(SignalDetection(50, 50, 50, 50), label="Random A")
        exp.add_condition(SignalDetection(30, 70, 20, 80), label="Random B")

        auc = exp.compute_auc()
        self.assertGreaterEqual(auc, 0)
        self.assertLessEqual(auc, 1)

if __name__ == "__main__":
    unittest.main()
#This code was assisted with the help of AI 