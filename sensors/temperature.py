import random


def read_temperature() -> float:
    """Simulate reading the ambient temperature in Celsius."""
    return round(random.uniform(20.0, 35.0), 2)
