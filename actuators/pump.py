PUMP_STATE = False


def pump_on():
    global PUMP_STATE
    PUMP_STATE = True
    print("[ACTUATOR] Pump turned ON")


def pump_off():
    global PUMP_STATE
    PUMP_STATE = False
    print("[ACTUATOR] Pump turned OFF")


def is_pump_on() -> bool:
    return PUMP_STATE
