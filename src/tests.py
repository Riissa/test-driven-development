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

    #This is for test_sorted_roc_points2
    def setUp(self):
        """Set up an Experiment instance and SignalDetection conditions before each test."""
        self.exp = Experiment()  # ✅ Define self.exp so all tests can use it
        self.sdt1 = SignalDetection(30, 10, 15, 25)  # ✅ Define test conditions
        self.sdt2 = SignalDetection(40, 20, 25, 15)

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
        #Test that sorted_roc_points() correctly returns sorted false alarm rates and hit rates.

        exp = Experiment()  # Create an Experiment instance

        # ✅ Test 1: Ensure it raises ValueError if no conditions exist
        with self.assertRaises(ValueError):
            exp.sorted_roc_points()

        # ✅ Create dynamic test cases (change values as needed)
        test_cases = [
            SignalDetection(50, 10, 30, 10),  # False Alarm Rate: 0.75, Hit Rate: 0.8333
            SignalDetection(20, 40, 10, 30),  # False Alarm Rate: 0.25, Hit Rate: 0.3333
            SignalDetection(30, 20, 20, 20),  # False Alarm Rate: 0.50, Hit Rate: 0.60
        ]

        # ✅ Extract expected values dynamically
        expected_false_alarm_rates = sorted([sdt.false_alarm_rate for sdt in test_cases])
        expected_hit_rates = [sdt.hit_rate for _, sdt in sorted(zip([sdt.false_alarm_rate for sdt in test_cases], test_cases))]

        # ✅ Add conditions dynamically
        for i, sdt in enumerate(test_cases):
            exp.add_condition(sdt, label=f"Condition {i+1}")

        # ✅ Get sorted ROC points
        false_alarm_rates, hit_rates = exp.sorted_roc_points()

    def test_sorted_roc_points2(self):
        #2nd version of the roc test...may not be needed later but keep it for now
        """Test that the ROC points are sorted by false alarm rate."""
        self.exp.add_condition(self.sdt1, label="Condition A")
        self.exp.add_condition(self.sdt2, label="Condition B")
        false_alarm_rate, hit_rate = self.exp.sorted_roc_points()

    # ✅ Check if sorted by false alarm rate
        self.assertTrue(all(false_alarm_rate[i] <= false_alarm_rate[i+1] for i in range(len(false_alarm_rate)-1)))

    


if __name__ == "__main__":
    unittest.main()
