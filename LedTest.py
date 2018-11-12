import RPi.GPIO as GPIO
import time

#define the LED pins
led_pin_green = 40
led_pin_yellow = 38
led_pin_red = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_yellow, GPIO.OUT)
GPIO.setup(led_pin_red, GPIO.OUT)

try:
    while True:
        #blink green led
        GPIO.output(led_pin_green,True)
        print("Green led ON")
        time.sleep(.5)
        GPIO.output(led_pin_green,False)
       
        #blink yellow led
        GPIO.output(led_pin_yellow,True)
        print("Yellow led ON")
        time.sleep(.5)
        GPIO.output(led_pin_yellow,False)

        #blink red led
        GPIO.output(led_pin_red,True)
        print("Red led ON")
        time.sleep(.5)
        GPIO.output(led_pin_red,False)

except KeyboardInterrupt:
    #turn leds OFF
    GPIO.output(led_pin_green,False)
    GPIO.output(led_pin_yellow,False)
    GPIO.output(led_pin_red,False)
    print("Keyboard interrupt, turn off all leds")

finally:
    GPIO.cleanup()
    print("clean up GPIO. Exiting program, Goodbye!!")
