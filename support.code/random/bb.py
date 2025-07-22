import pyfirmata2
from threading import Timer

class Blink():
    def __init__(self, board, seconds):
        self.digital_0 = board.get_pin('d:9:o')
        self.timer = None
        self.DELAY = seconds


    def blinkCallback(self):
        # call itself again so that it runs periodically
        self.timer = Timer(self.DELAY,self.blinkCallback)

        # start the timer
        self.timer.start()
        
        # now let's toggle the LED
        v = self.digital_0.read()
        v = not v
        if v:
            print("On")
        else:
            print("Off")
        self.digital_0.write(v)

    # starts the blinking
    def start(self):
        # Kickstarting the perpetual timer by calling the
        # callback function once
        self.blinkCallback()

    # stops the blinking
    def stop(self):
        # Cancel the timer
        self.timer.cancel()


PORT =  pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)

t = Blink(board,2)
t.start()

print("To stop the program press return.")
input()
t.stop()

# close the serial connection
board.exit()