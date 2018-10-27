import time
import serial

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0.1)

while True:
    x = raw_input()
    if x=='a':
        var = 'a'
        ser.write(bytes(var.encode('ascii')))
        while True:
            data = ser.readline()[:-2]
            if data:
                print(data)
            else:
                print("data not found")
    elif x=='b':
        var = 'b'
        ser.write(bytes(var.encode('ascii')))
    elif x=='c':
        var='c'
        ser.write(bytes(var.encode('ascii')))
    elif x=='d':
        var = 'd'
        ser.write(bytes(var.encode('ascii')))
