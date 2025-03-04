from SignalDetection import SignalDetection

class Experiment:
    def __init__(self):
        """Initialize an empty experiment with a list to store SDT objects and labels."""
        self.conditions = []
        self.labels = []

    def add_condition(self, sdt_obj, label=None):
        """Adds a SignalDetection object and an optional label to the experiment."""
        if not isinstance(sdt_obj, SignalDetection):
            raise TypeError("sdt_obj must be an instance of SignalDetection")
        self.conditions.append(sdt_obj)
        self.labels.append(label)

    def sorted_roc_points(self):
        """Returns sorted false alarm rates and hit rates for ROC curve plotting."""
        if not self.conditions:
            raise ValueError("No conditions have been added to the experiment.")

        # Extract false alarm rates and hit rates
        roc_points = [(cond.false_alarm_rate(), cond.hit_rate()) for cond in self.conditions]

        # Sort by false alarm rate (ascending)
        roc_points.sort()

        # Unpack into two separate lists
        false_alarm_rates, hit_rates = zip(*roc_points)

        return list(false_alarm_rates), list(hit_rates)
    
    def compute_auc(self):
        """Computes the Area Under the Curve (AUC) using the trapezoidal rule."""
        if not self.conditions:
            raise ValueError("No conditions have been added to the experiment.")

        false_alarm_rates, hit_rates = self.sorted_roc_points()

        # Compute AUC using the Trapezoidal Rule
        auc = 0
        for i in range(1, len(false_alarm_rates)):
            width = false_alarm_rates[i] - false_alarm_rates[i - 1]
            height = (hit_rates[i] + hit_rates[i - 1]) / 2
            auc += width * height  # Trapezoidal rule

        return auc
#This code was assisted with the help of AI 
