import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        """
        Initializes the SignalDetection object.
        """
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def hit_rate(self):
        """Dynamically calculates the hit rate."""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0 #should update instead of being stored once in init?

    def false_alarm_rate(self):
        """Dynamically calculates the false alarm rate."""
        total = self.falseAlarms + self.correctRejections
        return self.falseAlarms / total if total > 0 else 0

    def d_prime(self):
        """
        Calculates d-prime (d'), a measure of sensitivity in signal detection theory.

        Returns:
            float: The d-prime value.
        """
        H = self.hit_rate()  # Get latest hit rate
        FA = self.false_alarm_rate()  # Get latest false alarm rate

        try:
            z_hit = stats.norm.ppf(H)
            z_false_alarm = stats.norm.ppf(FA)
        except ValueError:
            return 0  # If invalid input to z-score calculation (0 or 1), return 0

        return z_hit - z_false_alarm

    def criterion(self):
        """
        Calculates the criterion (c), which measures the decision threshold.

        Returns:
            float: The criterion value.
        """
        H = self.hit_rate()  # Get latest hit rate
        FA = self.false_alarm_rate()  # Get latest false alarm rate

        try:
            z_hit = stats.norm.ppf(H)
            z_false_alarm = stats.norm.ppf(FA)
        except ValueError:
            return 0  # If invalid input to z-score calculation (0 or 1), return 0

        return -0.5 * (z_hit + z_false_alarm)


# Example usage
if __name__ == "__main__":
    sd = SignalDetection(15, 5, 15, 5)

    print(f"d-prime: {sd.d_prime():.2f}")
    print(f"criterion: {sd.criterion():.2f}")


