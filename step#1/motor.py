import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(7,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.setup(1,gpio.OUT)

pwm=gpio.PWM(8,100)
pwm1=gpio.PWM(7,100)
pwm2=gpio.PWM(1,100)

pwm.start(13)
pwm1.start(50)
pwm2.start(50)

def change(k):
    if k<0:
        k=0
    if k>100:
        k=100
    print("dc speed is",k-50)
    pwm1.ChangeDutyCycle(k)
    pwm2.ChangeDutyCycle(100-k)

def change1(angle): # 3~23
    if angle<3:
        angle=3
    if angle>23:
        anlge=23
    print("servo angle is",(angle-3)*9)
    pwm.ChangeDutyCycle(angle)

try:
    for i in range(0,100,10):
        change(i)
        time.sleep(1)
    for i in range(23,3,-1):
        change1(i)
        time.sleep(0.2)

    while True:
        k=float(raw_input("servo(0~180):"))
        change1(k/9+3)
        k=float(raw_input("dc(-50~50):"))+50
        change(k)
        
except KeyboardInterrupt:
    gpio.cleanup()
