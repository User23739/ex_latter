import os
import os.path
import glob
import cv2
import PIL
import numpy as np


CAPTCHA_IMAGE_FOLDER = "my_captcha_images"
OUTPUT_FOLDER = "my_letter_images"


# Get a list of all the captcha images we need to process
captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
counts = {}



def lineNoise(image):
    b = 2
    temp = cv2.CreateImage((image.width + 4, image.height + 4), image.depth, image.nChannels)
    result = cv2.CreateImage(cv2.GetSize(image), image.depth, image.nChannels)
    # IPL_BORDER_CONSTANT = 0
    # IPL_BORDER_REPLICATE = 1
    cv2.CopyMakeBorder(image, temp, (b, b), 0, 255)
    for x in range(b, image.width + b):
        for y in range(b, image.height + b):
            if temp[y + 1, x] == temp[y - 1, x] and \
                    temp[y + 2, x] == temp[y - 2, x] and \
                    temp[y + 1, x] == temp[y + 2, x] and \
                    temp[y, x] != temp[y + 1, x]:
                result[y - b, x - b] = temp[y + 1, x]
            elif temp[y, x + 1] == temp[y, x - 1] and \
                    temp[y, x + 2] == temp[y, x - 2] and \
                    temp[y, x + 1] == temp[y, x + 2] and \
                    temp[y, x] != temp[y, x + 1]:
                result[y - b, x - b] = temp[y, x + 1]
            else:
                result[y - b, x - b] = temp[y, x]
    return result











# loop over the image paths
for (i, captcha_image_file) in enumerate(captcha_image_files):
    print("[INFO] processing image {}/{}".format(i + 1, len(captcha_image_files)))

    # Since the filename contains the captcha text (i.e. "2A2X.png" has the text "2A2X"),
    # grab the base filename as the text
    filename = os.path.basename(captcha_image_file)
    #captcha_correct_text = os.path.splitext(filename)[0]

    print(filename)

    # Load the image and convert it to grayscale
    image = cv2.imread(captcha_image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    print('convert to grayscale')
    cv2.imshow("Output1", gray)
    cv2.waitKey()

    # Add some extra padding around the image
    gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)


    print('add arraud image')
    cv2.imshow("Output2", gray)
    cv2.waitKey()

    # threshold the image (convert it to pure black and white)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    print('threshhold')
    cv2.imshow('Output3', thresh)
    cv2.waitKey()

    lineNoise(thresh)






    cv2.waitKey()






