import pygame as pg
import Settings

class counter():
    def __init__(self, pos, pic, text):
        self.image = pic
        self.rect = self.image.get_rect(topleft = pos)
        self.text = str(text)

    def draw(self):
        Settings.screen.blit(self.image, self.rect)
        text = Settings.Fonts['counterFont'].render(self.text, 1, (12, 12, 12))
        Settings.screen.blit(text, text.get_rect(centery = self.rect.centery, left = self.rect.right + 10))

    def update(self):
        self.draw()


class button(pg.sprite.Sprite):
    def __init__(self, pos, w, h, text):
        super().__init__()
        self.image = pg.Surface((w, h))
        self.image.fill((227, 227, 227))
        self.rect = self.image.get_rect(topleft = pos)
        self.text = str(text)
        self.lastPress = pg.time.get_ticks()

    def isEnabled(self):
        pressed = pg.mouse.get_pressed()
        if (pg.time.get_ticks() - self.lastPress) > 200:
            self.lastPress = pg.time.get_ticks()
            if pressed[0]:
                pos = pg.mouse.get_pos()
                if self.rect.collidepoint(float(pos[0]), float(pos[1])):
                    return True
                else:
                    return False
            else:
                return False

    def draw(self):
        Settings.screen.blit(self.image, self.rect)
        text = Settings.Fonts['buttonFont'].render(self.text, 1, (0, 0, 0), (227, 227, 227))
        Settings.screen.blit(text, text.get_rect(center = self.rect.center))

    def update(self):
        self.draw()

class GUI():
    def __init__(self):
        #self.nextStepButton = button((Tilesize.TILESIZE * 16 + 16, 16), Settings.tile_size * 4 - 32, Tilesize.TILESIZE - 16, 'next step')
        #self.antCounter = counter((Tilesize.TILESIZE * 16, Tilesize.TILESIZE + 16), Settings.Images['antCounter'], MyGlobal_ISIS.ants)
        self.diamondCounter = counter((10, 10), pg.transform.scale(pg.image.load(Settings.Path['diamond']).convert_alpha(), (Settings.tile_size, Settings.tile_size)), '0')

    def updateCounters(self):
        self.diamondCounter.text = str(Settings.score)
        self.diamondCounter.update()

    def update(self):
        self.updateCounters()