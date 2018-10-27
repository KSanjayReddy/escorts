import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)

while True:
    x = raw_input()
    if x=='a':
        var = 'a'
        ser.write(bytes(var.encode('ascii')))
        #print(bytes(var.encode('ascii')))
        data = ser.readline()[:-2]
        if data:
            print(data)

    else:
        var = 'b'
        ser.write(bytes(var.encode('ascii')))
        #print(bytes(var.encode('ascii')))
