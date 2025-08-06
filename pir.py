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
            print("? Motion Detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()