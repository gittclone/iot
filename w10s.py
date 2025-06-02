import socket
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)  # PIR sensor

s = socket.socket()
port = 8787
s.bind(('', port))
s.listen(5)

print("Socket is listening...")

while True:
    c, addr = s.accept()
    print('Connection from:', addr)
    c.send('Thank you for connecting'.encode())

    while True:
        if GPIO.input(7):
            c.send("1".encode())
            print("Intruder Detected")
        else:
            c.send("0".encode())
            print("No Intruder")
