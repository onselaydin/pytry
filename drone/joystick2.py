import pygame
import time
pygame.joystick.init()
print(pygame.joystick.get_init())
print(pygame.joystick.get_count())
j =  pygame.joystick.Joystick(0)
print(j)
j.init()
print(j.get_init())
print(j.get_id())
for j in range(10):
    for i in range(0, j.get_numaxes()):
        print(j.get_axis(i))
        time.sleep(1)

pygame.joystick.quit()