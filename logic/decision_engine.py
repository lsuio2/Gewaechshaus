from __future__ import annotations
from datetime import datetime
from pathlib import Path
import yaml

from sensors import temperature, soil
from actuators import light, motor, pump

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_environment() -> dict:
    config = load_config()
    temp = temperature.read_temperature()
    moisture = soil.read_soil_moisture()

    # Temperature control
    if temp > config["thresholds"]["temperature_max"]:
        motor.open_flap()
    else:
        motor.close_flap()

    # Soil moisture control
    if moisture < config["thresholds"]["soil_moisture_min"]:
        pump.pump_on()
    else:
        pump.pump_off()

    # Light schedule
    schedule = config["light_schedule"]
    now = datetime.now().strftime("%H:%M")
    if schedule["start"] <= now <= schedule["end"]:
        light.light_on()
    else:
        light.light_off()

    return {
        "temperature": temp,
        "soil_moisture": moisture,
        "flap": motor.flap_state(),
        "pump": pump.is_pump_on(),
        "light": light.is_light_on(),
    }
