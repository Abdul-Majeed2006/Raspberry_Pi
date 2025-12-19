from machine import Pin, PWM, ADC
from time import sleep

# --- Hardware Setup ---
red_led = PWM(Pin(21))
blue_led = PWM(Pin(22))
green_led = PWM(Pin(20))

red_led.freq(1000)
blue_led.freq(1000)
green_led.freq(1000)

knob_1 = ADC(27)
knob_2 = ADC(26)
buzzer = Pin(9, Pin.OUT)

while 1:
    duty = 65535
    duty_2 = 0
    red_led.duty_u16(duty)
    green_led.duty_u16(duty_2)
    sleep(1)
    duty = 0
    duty_2 = 65535
    red_led.duty_u16(duty)
    green_led.duty_u16(duty_2)
    sleep(1)