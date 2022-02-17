import pygame as pg
from pygame.locals import *

pg.init()

import Settings

run = True
while run:

    Settings.clock.tick(Settings.fps)

    Settings.screen.blit(Settings.Images['background_image'], (0, 0))
    Settings.screen.blit(Settings.Images['sun_image'], (100, 100))

    Settings.player.update()
    Settings.world.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()