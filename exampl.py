from PIL import Image
import numpy as np


def lineNoise(image):
    b = 2
    temp = image
    result = image
    result.show()
    wi, hi = image.size

    for x in range(wi):
        for y in range(hi):
            if temp.getpixel((y + 1, x)) == temp.getpixel((y - 1, x)):
                print(temp.getpixel((y + 1, x)), "==", temp.getpixel((y - 1, x)))
                result.putpixel((y - b, x - b), temp.getpixel((y + 1, x)))
            elif temp.getpixel((y, x + 1)) == temp.getpixel((y, x - 1)):
                result.putpixel((y - b, x - b), temp.getpixel((y, x + 1)))
            else:
                result.putpixel((y - b, x - b), temp.getpixel((y, x)))
    return result
    # for x in range(b, wi + b):
    #     for y in range(b, hi + b):
    #         if temp.getpixel((y + 1, x)) == temp.getpixel((y - 1, x)) and \
    #             temp.getpixel((y + 2, x)) == temp.getpixel((y - 2, x)) and \
    #             temp.getpixel((y + 1, x)) == temp.getpixel((y + 2, x)) and \
    #             temp.getpixel((y, x)) != temp.getpixel((y + 1, x)):
    #             result.putpixel((y - b, x - b), temp.getpixel((y + 1, x)))
    #         elif temp.getpixel((y, x + 1)) == temp.getpixel((y, x - 1)) and \
    #             temp.getpixel((y, x + 2)) == temp.getpixel((y, x - 2)) and \
    #             temp.getpixel((y, x + 1)) == temp.getpixel((y, x + 2)) and \
    #             temp.getpixel((y, x)) != temp.getpixel((y, x + 1)):
    #             result.putpixel((y - b, x - b), temp.getpixel((y, x + 1)))
    #         else:
    #             result.putpixel((y - b, x - b), temp.getpixel((y, x)))
    # return result


try:

    img = Image.open('D:\py\ex_latter\my_captcha_images\scr11.png')

except FileNotFoundError:
    print("Файл не найден")

print(img.format, img.size, img.mode)

res = lineNoise(img)

res.show()

# wi, hi = img.size
#
# for i in range(wi):
#     for j in range(hi):
#         print(img.getpixel((i, j)))

#print(wi, hi)

#obj = img.load()
#print(obj)

#print(img.getpixel((1, 1)))





