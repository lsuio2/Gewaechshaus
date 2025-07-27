import random


def read_humidity() -> float:
    """Simulate reading the relative humidity in percent."""
    return round(random.uniform(40.0, 80.0), 2)
