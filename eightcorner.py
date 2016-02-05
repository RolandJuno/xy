# Implementation of Gerog Nees "Eight Corner"
import xy
import random
import math

def main():
    random.seed()
    paths = []
    columns = 14
    rows = 19
    sqrsize = 30
    padding = sqrsize * .2

    for y in range (1, rows+1):
        for x in range (1, columns+1):
            path = []
            for z in range (0, 8):
                x1 = random.uniform(0, sqrsize)
                y1 = random.uniform(0, sqrsize)
                path.append(((x1+sqrsize*x+padding*x),(y1+sqrsize*y+padding*y)))
                if (z==0):
                    x0 = x1
                    y0 = y1
            path.append(((x0+sqrsize*x+padding*x),(y0+sqrsize*y+padding*y))) # return to the start for closed path
            paths.append(path)
    drawing = xy.Drawing(paths).scale_to_fit(10365, 16640, 2000)
    centereddrawing = drawing.translate((10365-drawing.width)/2,(16640-drawing.height)/2)
    #drawing = drawing.sort_paths_greedy()
    xy.draw(centereddrawing)

if __name__ == '__main__':
    main()
