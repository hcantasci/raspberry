#!/usr/bin/python
import sys
import Adafruit_DHT
import os
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import time
from time import sleep

from RPLCD import CharLCD

k = 0
l = 0

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)
    

if temperature <= 100 :
    if k == 0 : 
        GPIO.output(23, GPIO.LOW)
        time.sleep(1)
        GPIO.output(23, GPIO.HIGH)
        k = 1
        l=0
    else:
        if l == 0:
            GPIO.output(23, GPIO.LOW)
            time.sleep(1)
            GPIO.output(23, GPIO.HIGH)
            k = 0
            print 'sicaklik24 uzeri'
            l = 1
    
