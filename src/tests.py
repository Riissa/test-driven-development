import sys
import os
import unittest

# Add 'src' to Python's module search path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Experiment import Experiment  # Adjust if needed based on folder structure
#NEW 
from SignalDetection import SignalDetection  # Adjust the import path if necessary

#Tests contructor (__init__) method
class TestExperiment(unittest.TestCase):
    def test_experiment_initialization(self):
        """Test that the Experiment constructor initializes an empty list."""
        exp = Experiment()  # Step 1: Create an Experiment object
        self.assertTrue(hasattr(exp, 'data'))  # Step 2: Check if 'data' exists
        self.assertIsInstance(exp.data, list)  # Step 3: Ensure 'data' is a list
        self.assertEqual(exp.data, [])  # Step 4: Ensure 'data' starts empty

    def test_add_condition(self):
        """Test that add_condition correctly adds a condition with its label."""
        exp = Experiment()  # Create a new Experiment instance
        # Create a SignalDetection object with some parameters.
        sdt = SignalDetection(40, 10, 20, 30)
        label = "Condition A"

        # Before adding, the data list should be empty.
        self.assertEqual(len(exp.data), 0)

        # Add the condition using the add_condition method.
        exp.add_condition(sdt, label=label)

        # After adding, there should be one condition in the data list.
        self.assertEqual(len(exp.data), 1)

        # Check that the condition stored has the correct contents.
        # This assumes add_condition stores a dictionary with keys 'sdt_obj' and 'label'.
        condition = exp.data[0]
        self.assertEqual(condition['sdt_obj'], sdt)
        self.assertEqual(condition['label'], label)


if __name__ == "__main__":
    unittest.main()
