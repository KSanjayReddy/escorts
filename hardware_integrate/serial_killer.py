import time

import serial

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0.1)
var = 'a'
time.sleep(3)
ser.write(bytes(var.encode('ascii')))
data = ser.readline()[:-2]
print(data)
while True:
    data = ser.readline()[:-2]
    if data:
        print(data)
    else:
        print("data not found")
