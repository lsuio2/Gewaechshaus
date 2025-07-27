import random


def read_soil_moisture() -> float:
    """Simulate reading soil moisture percentage."""
    return round(random.uniform(20.0, 60.0), 2)
