import RPi.GPIO as gpio
import time
import pygame
from pygame.locals import *

pwm_pin = 7
pwm_pin1 = 8
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pwm_pin, gpio.OUT)
gpio.setup(pwm_pin1, gpio.OUT)
pwm = gpio.PWM(pwm_pin, 100)
pwm1 = gpio.PWM(pwm_pin1, 100)
angle = 15
angle1 = 15
pwm.start(angle)
pwm1.start(angle1)

def init():
    for i in range(170,130,-1):
        pwm.ChangeDutyCycle(i/10)
        time.sleep(0.1)
        print(i/10)
    return 2

def contr():
    pygame.init()
    scren = pygame.display.set_mode((100, 100))
    cam=0
    out=3
    angle=15
    angle1=15
    while True:
        for event in pygame.event.get():
            if angle < 8:
                angle = 8
            elif angle > 22:
                angle = 22
            if angle1 > 22:
                angle1 = 22
            elif angle1 < 8:
                angle1 = 8
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    angle=angle+0.2
                elif event.key == K_DOWN:
                    if angle>=15:
                        time.sleep(0.8)
                    if angle==14:
                        time.sleep(1)
                        angle=13
                    else:
                        angle=angle-1
                elif event.key == K_RIGHT:
                    angle1=angle1-5
                elif event.key == K_LEFT:
                    angle1=angle1+5
                elif event.key == K_SPACE:
                    angle=15
                    angle1=15
                elif event.key == K_ESCAPE:
                    angle = 15
                    angle1 = 15
            pwm1.ChangeDutyCycle(angle1)
            pwm.ChangeDutyCycle(angle)
            print(angle,angle1)
    
#selection
try:
    choice=raw_input("init,cont:")
    if choice=="i":
        me=1
    if choice=="c":
        me=2
    if choice=="e":
        print('exit')
##init
    while me==1:
        me=init()
            
##control
    while me==2:
        me=contr()

except KeyboardInterrupt:
    gpio.cleanup()
