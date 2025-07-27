import random


def read_light() -> float:
    """Simulate reading the ambient light intensity in lux."""
    return round(random.uniform(100.0, 1000.0), 2)
