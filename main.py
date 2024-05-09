import cv2 as cv
import os
import time
#ascii symbols, ordered from darkest to lightest
ascii = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

#clears console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

camera = cv.VideoCapture(0)

while True:
    time.sleep(0.1)
    cls()
    frame = camera.read()
    gray_frame = cv.cvtColor(frame[1], cv.COLOR_BGR2GRAY)
    fin = cv.resize(gray_frame,(32,32))
    # waits .1 seconds, clears console, then convert the camera input to grayscale and 32 by 32 to make it easier to convert each pixel to an ASCII character
    for i in range(len(list(fin))):
        print('')
        #everytime the the loop goes to the next row, it also goes to a new row in the console
        for j in range(len(list(fin)[i])):
            # checks the pixels rgb color value. since its grayscale theres only one value (255 = white, 0 = black). if its brighter, the smaller ascii element is printed
            if fin[i][j] >= 232:
                print('.',end=' ')
            elif fin[i][j] >= 209:
                print(',',end=' ')
            elif fin[i][j] >= 186:
                print(':',end=' ')
            elif fin[i][j] >= 163:
                print(';',end=' ')
            elif fin[i][j] >= 140:
                print('+',end=' ')
            elif fin[i][j] >= 117:
                print('*',end=' ')
            elif fin[i][j] >= 94:
                print('?',end=' ')
            elif fin[i][j] >= 71:
                print('%',end=' ')
            elif fin[i][j] >= 48:
                print('#',end=' ')
            elif fin[i][j] >= 25:
                print('@',end=' ')
            else:
                print(' ',end=' ')