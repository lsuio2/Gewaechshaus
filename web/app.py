from flask import Flask, render_template, request, redirect, Response, stream_with_context
from pathlib import Path
import yaml
import json
import time

from logic import decision_engine

app = Flask(__name__)
CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_config(data):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f)


@app.route("/stream")
def stream():
    """Stream environment data every 5 seconds using Server-Sent Events."""

    def event_stream():
        while True:
            env = decision_engine.check_environment()
            yield f"data: {json.dumps(env)}\n\n"
            time.sleep(5)

    return Response(stream_with_context(event_stream()), mimetype="text/event-stream")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        config = load_config()
        config["thresholds"]["temperature_max"] = float(request.form.get("temperature_max"))
        config["thresholds"]["soil_moisture_min"] = float(request.form.get("soil_moisture_min"))
        config["light_schedule"]["start"] = request.form.get("light_start")
        config["light_schedule"]["end"] = request.form.get("light_end")
        save_config(config)
        return redirect("/")

    env = decision_engine.check_environment()
    config = load_config()
    return render_template("index.html", env=env, config=config)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
