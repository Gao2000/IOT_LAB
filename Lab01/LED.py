import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)
s = [1,1,1]
o = [3,3,3]

"""
while True:
    print("LED is on")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    print("LED is off")
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
"""

while True:
    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        print(s[i])
        time.sleep(s[i])
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
    
    time.sleep(2)

    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        print(o[i])
        time.sleep(o[i])
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

    time.sleep(2)

    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        print(s[i])
        time.sleep(s[i])
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
    print("one letter")
    time.sleep(6)

    
GPIO.cleanup()
