import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while True:
    if GPIO.input(11):
        GPIO.output(3, GPIO.HIGH)
        print("Intruder Detected!!")
    else:
        GPIO.output(3, GPIO.LOW)
        print("No Intruder")
