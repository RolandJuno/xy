# Changes for HP 7475A Plotter via RS-232
# You will need a special cable to connect your plotter.
# http://music.columbia.edu/cmc/chiplotle/manual/_static/SerialPlotterCable_Chiplotle.pdf
import serial
import time

PORT = '/dev/tty.usbserial-FTBRY656'
BAUD = 9600

UP = 0
DOWN = 50

class Device(object):

    def __init__(self, port=PORT, baud=BAUD, up=UP, down=DOWN, verbose=False):
        self.serial = serial.Serial(port, baud, dsrdtr=True, rtscts=True) if port else None
        self.up = up
        self.down = down
        self.verbose = verbose

    def read(self):
        data = []
        while True:
            c = self.serial.read(1) if self.serial else '\n'
            if c == '\n':
                return ''.join(data)
            data.append(c)

    def write(self, *args):
        line = ' '.join(map(str, args))
        if self.verbose:
            print line
        if self.serial:
            self.serial.write(line),
        self.serial.flush()
        return
        response = self.read()
        if self.verbose:
            print response

    def home(self):
        self.write(';IN;SP1;VS10;PU;') #VS10 will slow it down some (35 is normal)
        self.write(chr(27)+'.R')

    def move(self, x, y):
        # swap x and y since y runs along the short edge of the page for 11 x 17 "ledger" paper
        self.write(y, ',', x, ',')

    def pen(self, position):
        if position is UP:
            self.write(';PU')
        elif position is DOWN:
            self.write(';PD')

    def pen_up(self):
        self.pen(self.up)

    def pen_down(self):
        self.pen(self.down)

    def draw(self, points, up=None, down=None):
        if not points:
            return
        self.pen(self.up if up is None else up)
        self.move(*points[0])
        self.pen(self.down if down is None else down)
        for point in points:
            self.move(*point)
        self.pen(up)

    def gcode(self, g):
        for line in g.lines:
            self.write(line)
