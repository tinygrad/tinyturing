from display import Display
import pygame
import logging
logging.basicConfig(level=logging.INFO)

# initialize
display = Display("/dev/ttyACM1")
display.clear()

# put logo
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (400, 240))
display.blit(logo, (200, 25))

# text
text = display.text(f"zZzZz", 100, True, (255, 255, 255))
display.blit(text, (400 - text.get_width() // 2, 220 + (120 - text.get_height() // 2)))

display.flip()

display.clear()

# put logo
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (400, 240))
display.blit(logo, (200, 25))

# text
text = display.text(f"...", 100, True, (255, 255, 255))
display.blit(text, (400 - text.get_width() // 2, 220 + (120 - text.get_height() // 2)))

display.flip()

display.clear()

# put logo
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (400, 240))
display.blit(logo, (200, 25))

# text
text = display.text(f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 100, True, (255, 255, 255))
display.blit(text, (400 - text.get_width() // 2, 220 + (120 - text.get_height() // 2)))

display.flip()
