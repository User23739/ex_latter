


import numpy as np
import sys
import cv2 as cv

path = 'D:\py\ex_latter\my_captcha_images\scr13.png'


def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)

# Load image
try:

    img = cv.imread(path, cv.IMREAD_COLOR)

except FileNotFoundError:
    print("Файл не найден")

# Show source image
cv.imshow("Origin", img)


# Convert to gray
if len(img.shape) != 2:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
else:
    gray = img
# Show gray image
show_wait_destroy("gray", gray)

# Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
gray = cv.bitwise_not(gray)

show_wait_destroy("gray2", gray)



bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
# Show binary image
show_wait_destroy("binary", bw)

# construct a closing kernel and apply it to the thresholded image
kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
closed = cv.morphologyEx(bw, cv.MORPH_CLOSE, kernel)

# Show closed image
show_wait_destroy("closed", closed)


# # perform a series of erosions and dilations
# closed = cv.erode(closed, None, iterations = 4)
# closed = cv.dilate(closed, None, iterations = 4)
#
# show_wait_destroy("closed2", closed)

# construct a opening kernel and apply it to the closenig image
kernel_2 = cv.getStructuringElement(cv.MORPH_RECT, (2, 3))
opend = cv.morphologyEx(closed, cv.MORPH_OPEN, kernel_2)

# Show closed image
show_wait_destroy("opend", opend)

# construct a closing kernel and apply it to the thresholded image
kernel_3 = cv.getStructuringElement(cv.MORPH_RECT, (3, 4))
closed_2 = cv.morphologyEx(opend, cv.MORPH_CLOSE, kernel_3)

# Show closed image
show_wait_destroy("closed_2", closed_2)

# Add some extra padding around the image
#borders = cv.copyMakeBorder(closed_2, 20, 20, 20, 20, cv.BORDER_REPLICATE)

# Show borders image
#how_wait_destroy("borders", borders)

# threshold the image (convert it to pure black and white)
thresh = cv.threshold(closed_2, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]

# Show borders image
show_wait_destroy("thresh", thresh)

# find the contours (continuous blobs of pixels) the image
contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]

print(contours)
cv.drawContours(img, contours, -1, (0, 0, 255), 3)

# Show borders image
show_wait_destroy("out", img)