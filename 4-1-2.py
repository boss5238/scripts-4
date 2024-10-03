import RPi.GPIO as GPIO
from time import sleep


def dec_to_bin(number):
    return [int(x) for x in bin(number)[2:].zfill(8)]


dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        t = input()
        if t == 'q':
            break
        if not t.isdigit() or float(t) < 0:
            print('Введите положительное число')
        else:
            t = int(t)
            for i in range(0, 256):
                GPIO.output(dac, dec_to_bin(i))
                print(3.3 / (2 ** 8) * i)
                sleep(t / 512)
            for i in range(255, -1, -1):
                GPIO.output(dac, dec_to_bin(i))
                print(3.3 / (2 ** 8) * i)
                sleep(t / 512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()