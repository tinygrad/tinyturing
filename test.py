from bdffont import BdfFont
import numpy as np

font = BdfFont.load("/tmp/spleen-2.1.0/spleen-32x64.bdf")

print(f'name: {font.name}')
print(f'size: {font.point_size}')
print(f'ascent: {font.properties.font_ascent}')
print(f'descent: {font.properties.font_descent}')
print()

bitmaps = []

for glyph in font.get_glyphs():
  # only print ascii characters
  if glyph.code_point < 32 or glyph.code_point > 126:
    continue
  bitmaps.append(glyph.bitmap)
  for bitmap_row in glyph.bitmap:
    text = ''.join(map(str, bitmap_row)).replace('0', '  ').replace('1', '██')
    print(f'{text}*')
  print()

bitmaps = np.array(bitmaps)
np.save('font.npy', bitmaps)
