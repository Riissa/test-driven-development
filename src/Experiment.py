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
