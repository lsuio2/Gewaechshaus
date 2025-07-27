# Gewaechshaus

Dieses Projekt steuert ein kleines Gewächshaus mit dem Raspberry Pi. Es sammelt Sensordaten,
steuert Aktoren und bietet ein einfaches Webinterface zum Anpassen von Schwellenwerten.

Die Hardware ist noch nicht vorhanden, daher werden Sensorwerte simuliert.

## Projektstruktur

- `main.py` – Einstiegspunkt zum Testen der Logik
- `config.yaml` – Konfiguration für Schwellenwerte und Lichtzeiten
- `sensors/` – Module zum Lesen der (simulierten) Sensorwerte
- `actuators/` – Module zur Steuerung von Licht, Motor und Pumpe
- `logic/` – Entscheidungsengine
- `web/` – Einfaches Flask-Webinterface
- `data/` – Ablage für Logs und Kamerabilder

## Installation

```bash
pip install -r requirements.txt
```

## Starten

```bash
python main.py        # einmalige Messung und Bildaufnahme
python web/app.py     # Weboberfläche
```
