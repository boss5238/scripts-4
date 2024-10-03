import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
p = GPIO.PWM(21, 1000)
p.start(0)
try:
    while True:
        duty_cycle = input()
        if duty_cycle == 'q':
            break
        if not duty_cycle.isdigit() or int(duty_cycle) < 0 or \
            int(duty_cycle) not in range(0, 101):
            print('Введите число из дипазона 0-100')
        else:
            duty_cycle = int(duty_cycle)
            p.ChangeDutyCycle(duty_cycle)
finally:
    GPIO.cleanup()