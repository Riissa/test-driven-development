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

    def test_sorted_roc_points(self):
        """Test that sorted_roc_points() correctly returns sorted false alarm rates and hit rates."""

        exp = Experiment()  # Create an Experiment instance

        # Test 1: Ensure it raises ValueError if no conditions exist
        with self.assertRaises(ValueError):
            exp.sorted_roc_points()

     # Create multiple SignalDetection objects with varying false alarm and hit rates
        sdt1 = SignalDetection(40, 10, 20, 30)  # False Alarm Rate: 0.4, Hit Rate: 0.8
        sdt2 = SignalDetection(20, 20, 10, 40)  # False Alarm Rate: 0.2, Hit Rate: 0.5
        sdt3 = SignalDetection(10, 30, 5, 55)   # False Alarm Rate: 0.0833, Hit Rate: 0.25

     # Add conditions to the experiment
        exp.add_condition(sdt1, label="Condition 1")
        exp.add_condition(sdt2, label="Condition 2")
        exp.add_condition(sdt3, label="Condition 3")

     # Get sorted ROC points
        false_alarm_rates, hit_rates = exp.sorted_roc_points()

        # Expected sorted false alarm rates and corresponding hit rates
        expected_false_alarm_rates = [0.0833, 0.2, 0.4]
        expected_hit_rates = [0.25, 0.5, 0.8]

      # Ensure lists are sorted and match expected values
        self.assertEqual(false_alarm_rates, expected_false_alarm_rates)
        self.assertEqual(hit_rates, expected_hit_rates)

        # Ensure lists are the same length
        self.assertEqual(len(false_alarm_rates), len(hit_rates))


    

if __name__ == "__main__":
    unittest.main()
