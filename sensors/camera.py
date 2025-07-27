from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


IMAGES_DIR = Path(__file__).resolve().parents[1] / "data" / "images"


def capture_image() -> Path:
    """Capture a dummy image and store it in the images directory."""
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = IMAGES_DIR / f"image_{timestamp}.jpg"

    # Create a simple placeholder image with the timestamp
    img = Image.new("RGB", (640, 480), color="green")
    draw = ImageDraw.Draw(img)
    text = f"{timestamp}"
    draw.text((10, 10), text, fill="white")
    img.save(image_path)
    return image_path
