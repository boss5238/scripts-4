import RPi.GPIO as GPIO


def dec_to_bin(number):
    return [int(x) for x in bin(number)[2:].zfill(8)]


dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        input1 = input()
        if input1 == 'q':
            break
        elif '.' in input1 or ',' in input1:
            print('Введите целое число')
        elif not input1.isdigit() or int(input1) not in range(0, 256):
            print('Введите число из диапазона 0-255')
        else:
            n = int(input1)
            GPIO.output(dac, dec_to_bin(n))
            print(3.3 / (2 ** 8) * n)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()