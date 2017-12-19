#!/usr/bin/python3
# encoding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

def blink():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.3)

if __name__ == '__main__':
    i = 0;
    print("Start to blink");
    while(i < 1):
        blink()
        i = i + 1
    print("Stop to blink");
    GPIO.cleanup()
