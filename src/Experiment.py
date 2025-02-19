from src.SignalDetection import SignalDetection

from src.SignalDetection import SignalDetection

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
