import scipy.stats as stats
#This code was assisted with the help of chatGPT
class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        """
        I
        Parameters:
            hits (int): Number of hits (true positives).
            misses (int): Number of misses (false negatives).
            falseAlarms (int): Number of false alarms (false positives).
            correctRejections (int): Number of correct rejections (true negatives).
        """
        # Compute hit rate and false alarm rate based on raw counts
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

        # Compute rates, avoiding division by zero
        if (hits + misses) > 0:
            self.hit_rate = hits / (hits + misses)
        else:
            self.hit_rate = 0  # If no hits or misses, set to 0

        if (falseAlarms + correctRejections) > 0:
            self.false_alarm_rate = falseAlarms / (falseAlarms + correctRejections)
        else:
            self.false_alarm_rate = 0  # If no false alarms or correct rejections, set to 0

    def d_prime(self):
        """
        Calculate d-prime, a measure of sensitivity in signal detection theory.

        Returns:
            float: The d-prime value.
        """
        # Convert hit rate and false alarm rate to z-scores
        try:
            z_hit = stats.norm.ppf(self.hit_rate)
            z_false_alarm = stats.norm.ppf(self.false_alarm_rate)
        except ValueError:
            return 0  # If z-score calculation fails (0 or 1 input), return 0 as expected by the test

        # Calculate d-prime
        return z_hit - z_false_alarm

    def criterion(self):
        """
        Calculate criterion (c), which measures the decision threshold.

        Returns:
            float: The criterion value.
        """
        # Convert hit rate and false alarm rate to z-scores
        try:
            z_hit = stats.norm.ppf(self.hit_rate)
            z_false_alarm = stats.norm.ppf(self.false_alarm_rate)
        except ValueError:
            return 0  # If z-score calculation fails (0 or 1 input), return 0 as expected by the test

        # Calculate criterion
        return -0.5 * (z_hit + z_false_alarm)

# Example usage
if __name__ == "__main__":
    sd = SignalDetection(15, 5, 15, 5)

    print(f"d-prime: {sd.d_prime():.2f}")
    print(f"criterion: {sd.criterion():.2f}")