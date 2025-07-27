LIGHT_STATE = False


def light_on():
    global LIGHT_STATE
    LIGHT_STATE = True
    print("[ACTUATOR] Light turned ON")


def light_off():
    global LIGHT_STATE
    LIGHT_STATE = False
    print("[ACTUATOR] Light turned OFF")


def is_light_on() -> bool:
    return LIGHT_STATE
