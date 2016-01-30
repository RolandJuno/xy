# Conversion from Porcessing tutorial by Jim Plaxco
# http://www.artsnova.com/Nees_Schotter_Tutorial.html
import xy
import random
import math

def main():
    random.seed()
    paths = []
    columns = 24
    rows = 36
    sqrsize = 30
    h = sqrsize/2
    step = .22
    randsum = 0
    dampen = 0.45

    for y in range (1, rows+1):
        randsum = randsum + (y * step)
        for x in range (1, columns+1):
            path = []
            randval = random.uniform(-randsum, randsum)

            c = math.cos(math.radians(randval))
            s = math.sin(math.radians(randval))
            x1 = (x*sqrsize)+(randval*dampen)
            y1 = (y*sqrsize)+(randval*dampen)

            #http://stackoverflow.com/questions/644378/drawing-a-rotated-rectangle
            #sqrsize/2 for rotating about the center of the square
            path.append((( x1 + h * c - h * s ), ( y1 + h * c + h * s )))#ul
            path.append((( x1 - h * c - h * s ), ( y1 + h * c - h * s )))#ur
            path.append((( x1 - h * c + h * s ), ( y1 - h * c - h * s )))#br
            path.append((( x1 + h * c + h * s ), ( y1 - h * c + h * s )))#bl
            path.append((( x1 + h * c - h * s ), ( y1 + h * c + h * s )))#ul

            paths.append(path)
    drawing = xy.Drawing(paths).scale_to_fit(10365, 16640, 2000)
    centereddrawing = drawing.translate((10365-drawing.width)/2,(16640-drawing.height)/2)
    #drawing = drawing.sort_paths_greedy()
    xy.draw(centereddrawing)

if __name__ == '__main__':
    main()
