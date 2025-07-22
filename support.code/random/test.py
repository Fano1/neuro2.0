import pyfirmata2
import random

PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)


servo_5 = board.get_pin('d:9:s')

v = board.get_pin('a:1:i')

while(1):
    v = float(input("Servo angle from 0 to 180 degrees: "))
    servo_5.write(v)


board.exit()