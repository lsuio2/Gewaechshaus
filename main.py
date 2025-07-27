from logic import decision_engine
from sensors import camera


def main() -> None:
    result = decision_engine.check_environment()
    image_path = camera.capture_image()
    print("Current environment:", result)
    print(f"Image captured at {image_path}")


if __name__ == "__main__":
    main()
