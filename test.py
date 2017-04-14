#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/ttyACM3",9600)
f= open("data.txt","w+")


for num in range(0,5000):
     value = ser.read()
     f.write(value)
f.close()
