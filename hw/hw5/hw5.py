######################################################
# Name   : Jason Qiu
# Pledge : I pledge my honor that I have abided by the Stevens Honor System.
######################################################
from cs5png import PNGImage

def mult(c,n):
    '''Given numbers c and n, return c*n, using only addition and lööps'''
    out = 0
    if i >= 0:
        for i in range(n):
            out += c
    else:
        for i in range(abs(n)):
            for i in range(n):
                out -= c
    return out
def update(c,n):
    '''Given numbers c and n,
    return z where z(0, c) = z and z(n, c) = z(n-1, c)**2 + c,
    absolutely no recursion'''
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    '''Given a complex c and a number n, return if the magnitude of z
    never goes above 2 in the process of doing update(...). Don't(!)
    call update'''
    z = c
    for i in range(n):
        z = z**2 + c
        if abs(z) >2:
            return False
    return True

def scale(pix, pixelMax, floatMin, floatMax):
    '''Given a pixel value, the max pixel value,
    return where that pixel lies on [floatMin, floatMax] where
    pix=0 -> floatMin and pix=pixelMax -> floatMax'''
    return (pix/pixelMax)*(floatMax-floatMin) + floatMin

def mset(n):
    '''Creates a 300x200 image of the Mandelbrot set, where
    the image is of the complex plane with x real [-2, 1] and y imaginary, [-i, i]'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2., 1.)
            y = scale(row, height, -1.,1.)
            c = x+y*1j
            if inMSet(c, 25):
                # print(c)
                image.plotPoint(col,row)
    image.saveFile()

if __name__ == "__main__":
    iterations = 100 # Change this to play with the picture, once everything's working
    mset(iterations)