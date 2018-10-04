from PIL import Image

img = Image.open('Brain.jpg')

[img.quantize(colors=2**i, method=1).save(str(i) + "_bit.png") for i in range(1, 8)]

