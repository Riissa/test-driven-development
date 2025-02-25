from scipy.stats import norm

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        """Initialize SignalDetection object with given counts."""
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def hit_rate(self):
        """Returns the hit rate H = hits / (hits + misses)."""
        return self.hits / (self.hits + self.misses) if (self.hits + self.misses) > 0 else 0

    def false_alarm_rate(self):
        """Returns the false alarm rate FA = false alarms / (false alarms + correct rejections)."""
        return self.falseAlarms / (self.falseAlarms + self.correctRejections) if (self.falseAlarms + self.correctRejections) > 0 else 0

    def d_prime(self):
        """Computes d' (sensitivity index)."""
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        return norm.ppf(H) - norm.ppf(FA)

    def criterion(self):
        """Computes the decision criterion C."""
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        return -0.5 * (norm.ppf(H) + norm.ppf(FA))
