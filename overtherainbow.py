import math, colorsys
from PIL import Image, ImageDraw

img = Image.new('RGB', (128, 128))
d = ImageDraw.Draw(img)

d.setfill(onoff=True)
d.fill

#d.line([x1, y1, x2, y2], (R, G, B), depth)
img.show()
img.save("overtherainbow/overtherainbow.gif", "GIF")