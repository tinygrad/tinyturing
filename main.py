from display import Display
from PIL import Image
import numpy as np
import logging, random, time
logging.basicConfig(level=logging.INFO)

# initialize
display = Display("/dev/ttyACM1")
display.clear()

logo = Image.open("logo.png").convert("RGBA")
logo = logo.resize((400, 154))
logo = np.array(logo).transpose(1, 0, 2)

speed_x, speed_y = 1, 0
x, y = random.randint(0, 400), random.randint(0, 240)
while True:
  display.blit(logo, (x, y))
  if x + speed_x < 0 or x + speed_x > 400:
    speed_x *= -1
  if y + speed_y < 0 or y + speed_y > 480 - 154:
    speed_y *= -1
  x += speed_x
  y += speed_y
  st = time.perf_counter()
  display.flip()
  print(time.perf_counter() - st)
  display.clear()
