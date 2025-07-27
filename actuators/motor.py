MOTOR_STATE = "closed"


def open_flap():
    global MOTOR_STATE
    MOTOR_STATE = "open"
    print("[ACTUATOR] Flap opened")


def close_flap():
    global MOTOR_STATE
    MOTOR_STATE = "closed"
    print("[ACTUATOR] Flap closed")


def flap_state() -> str:
    return MOTOR_STATE
