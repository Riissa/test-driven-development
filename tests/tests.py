import unittest

from src.Experiment import Experiment  # Adjust if needed based on folder structure

#Tests contructor (__init__) method
class TestExperiment(unittest.TestCase):
    def test_experiment_initialization(self):
        """Test that the Experiment constructor initializes an empty list."""
        exp = Experiment()  # Step 1: Create an Experiment object
        self.assertTrue(hasattr(exp, 'data'))  # Step 2: Check if 'data' exists
        self.assertIsInstance(exp.data, list)  # Step 3: Ensure 'data' is a list
        self.assertEqual(exp.data, [])  # Step 4: Ensure 'data' starts empty

if __name__ == "__main__":
    unittest.main()
