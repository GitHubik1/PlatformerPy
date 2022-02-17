from token import SLASHEQUAL
import pygame as pg
import Settings
from os import walk

def import_folder(path):
    surfaceList = []

    for _, __, img_file in walk(path):
        for image in img_file:
            fullPath = path + '/' + image
            imageSurf = pg.transform.scale(pg.image.load(fullPath).convert_alpha(), (Settings.tile_size, Settings.tile_size))
            surfaceList.append(imageSurf)

    return surfaceList

class block(pg.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        try:
            self.image = pg.transform.scale(pg.image.load(path), (Settings.tile_size, Settings.tile_size))
        except FileNotFoundError:
            self.image = pg.transform.scale(pg.image.load('img/NotTexture.png'), (Settings.tile_size, Settings.tile_size))
        except TypeError:
            self.image = pg.transform.scale(pg.image.load('img/NotTexture.png'), (Settings.tile_size, Settings.tile_size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        pass

class spawnpoint(block):
    def __init__(self, pos, path):
        super().__init__(pos, path)
        self.actived = False
    
    def update(self):
        pass

class slime(block):
    def __init__(self, pos, path):
        super().__init__(pos, path)
    
    def update(self):
        if self.rect.colliderect(pg.Rect(Settings.player.pos.x, Settings.player.pos.y + 2, Settings.player.rect.width, Settings.player.rect.height)):
            if Settings.player.vel_y > 1 or Settings.player.vel_y < -1:
                Settings.player.vel_y = -(Settings.player.vel_y * 2)

class item(pg.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        try:
            self.images = import_folder(path)
        except FileNotFoundError:
            self.images = [pg.transform.scale(pg.image.load('img/NotTexture.png'), (Settings.tile_size, Settings.tile_size))]
        except TypeError:
            self.images = [pg.transform.scale(pg.image.load('img/NotTexture.png'), (Settings.tile_size, Settings.tile_size))]
        self.AnimSpeed, self.AnimNow, self.AnimCount = 500, 0, len(self.images)
        self.lastTimer, self.nowTimer = pg.time.get_ticks(), pg.time.get_ticks()

        self.image = self.images[self.AnimNow]
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        self.nowTimer = pg.time.get_ticks()
        if (self.nowTimer - self.lastTimer) > self.AnimSpeed:
            self.lastTimer = pg.time.get_ticks()
            self.AnimNow += 1
            if self.AnimNow + 1 > self.AnimCount:
                self.AnimNow = 0
            self.image = self.images[self.AnimNow]
        if self.rect.colliderect(Settings.playerRect):
            self.kill()
            Settings.score += 10