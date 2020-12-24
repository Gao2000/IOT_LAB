
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

sensor = 11
pin = 4

GPIO.setwarnings(False)

#v = 343
TRIG = 16
E    = 18
LED  = 12

print '1'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E,    GPIO.IN)
GPIO.setup(LED,  GPIO.OUT)
GPIO.output(TRIG,GPIO.LOW)

def measure(T):
    v = 331 + 0.6 * T
    print('{0} = 331 + 0.6 * {1}'.format(v, T)) 
#    st = "v = 331 + 0.6 * "
#    print(st, T)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    pulse_start = 0
    pulse_end   = 0
    while GPIO.input(E) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start
    d = t * v
    d = d / 2
    return d * 100

while(1):
    #
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)) 
    else:
        print('Failed to get reading. Try again!')
    ########

    print "next"
    m = measure(temperature)
    print m
    if m < 10:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(5)
    elif m >= 10 and m <= 20:
        for i in range(5):
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)            
    print "end"
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
