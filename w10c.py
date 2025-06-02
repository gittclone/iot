import socket
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.LOW)

s = socket.socket()
port = 8787
s.connect(('192.168.21.232', port))

print(s.recv(1024).decode())

while True:
    data = s.recv(1024).decode()
    if data == '1':
        print('Intruder detected')
        GPIO.output(8, GPIO.HIGH)
        sleep(10)
    else:
        GPIO.output(8, GPIO.LOW)
        print('Intruder not detected')

s.close()
