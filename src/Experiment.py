class Experiment:
    def __init__(self):
        self.data = []  # Initialize an empty list
        
    def add_condition(self, sdt_obj, label=None):
        """
        Adds a SignalDetection object with an optional label to the experiment.

        Parameters:
            sdt_obj (SignalDetection): The SignalDetection condition to add.
            label (str, optional): A description for the condition.
        """
        self.data.append({"sdt_obj": sdt_obj, "label": label})

    def sorted_roc_points(self):
        """Returns sorted false alarm rates and hit rates for plotting the ROC curve."""

        # If no conditions exist, raise a ValueError
        if not self.data:
            raise ValueError("No conditions available to generate ROC points.")

        # Extract false alarm rates and hit rates
        false_alarm_rates = []
        hit_rates = []

        for condition in self.data:
            sdt = condition["sdt_obj"]
            false_alarm_rates.append(sdt.false_alarm_rate)
            hit_rates.append(sdt.hit_rate)

        # Sort by false alarm rates and reorder hit rates accordingly
        sorted_pairs = sorted(zip(false_alarm_rates, hit_rates))
        sorted_false_alarm_rates, sorted_hit_rates = zip(*sorted_pairs)

        return list(sorted_false_alarm_rates), list(sorted_hit_rates)
