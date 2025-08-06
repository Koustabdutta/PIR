# 🔍 Raspberry Pi Motion Detection System with PIR Sensor, LED & Buzzer

This project uses a **PIR motion sensor**, an **HXD active buzzer**, and an **LED** connected to a **Raspberry Pi 3B** to detect motion and provide real-time alerts with sound and light.

## 📸 Features

- Motion detection using PIR sensor
- Audible alert with HXD active buzzer
- Visual alert with LED
- Clean GPIO handling
- Easily expandable (e.g., send email, log motion, etc.)

---

## 🧰 Hardware Required

| Component          | Quantity |
|--------------------|----------|
| Raspberry Pi 3B    | 1        |
| PIR Motion Sensor (HC-SR501) | 1 |
| HXD Active Buzzer  | 1        |
| LED                | 1        |
| 220Ω Resistor      | 1        |
| Jumper wires       | ~10      |
| Breadboard (optional) | 1     |

---

## 🔌 Wiring Diagram

| Component     | GPIO Pin (BCM) | Physical Pin |
|---------------|----------------|--------------|
| PIR OUT       | GPIO17         | Pin 11       |
| LED + (with 220Ω resistor) | GPIO18         | Pin 12       |
| Buzzer +      | GPIO27         | Pin 13       |
| All GNDs      | GND            | Pin 6, 9, or 14 |
| PIR VCC       | 5V             | Pin 2        |

---

## 🐍 Python Script

### `pir_alarm.py`

```python
import RPi.GPIO as GPIO
import time

PIR_PIN = 17        # PIR sensor output
LED_PIN = 18        # LED
BUZZER_PIN = 27     # HXD active buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("Initializing PIR sensor...")
time.sleep(2)
print("System Ready")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("🚨 Motion Detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
