import pygame as pg
import Settings

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.counter = 0
        self.image = pg.transform.scale(pg.image.load(f'img/guy1.png'), (24, 96))
        self.rect = self.image.get_rect(x = x, y = y)
        self.pos = self.image.get_rect()
        self.pos.x = x + Settings.tile_size * 7
        self.pos.y = y + Settings.tile_size * 22
        self.startX = x + Settings.tile_size * 7
        self.startY = y + Settings.tile_size * 22
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 1

    def update(self):
        dx = 0
        dy = 0

        last_direction = self.direction

        #get keypresses
        key = pg.key.get_pressed()
        if key[pg.K_SPACE] and self.jumped == False:
            self.vel_y = -Settings.JUMPPOWER
            self.jumped = True
        if key[pg.K_LEFT]:
            dx -= Settings.SPEED
            self.counter += 1
            self.direction = -1
        if key[pg.K_RIGHT]:
            dx += Settings.SPEED
            self.counter += 1
            self.direction = 1
        if key[pg.K_LEFT] == False and key[pg.K_RIGHT] == False:
            self.counter = 0
            self.index = 0

        #add gravity
        self.vel_y += Settings.GRAVITY
        dy += self.vel_y

        if(self.direction != last_direction):
            self.image = pg.transform.flip(self.image, True, False)

        #check for collision
        for tile in (list(Settings.tile_list) + list(Settings.spawnpoints)):
            #check for collision in x direction
            if tile.rect.colliderect(self.pos.x + dx, self.pos.y, self.width, self.height):
                dx = 0
            #check for collision in y direction
            if tile.rect.colliderect(self.pos.x, self.pos.y + dy, self.width, self.height):
                #check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile.rect.bottom - self.pos.top
                    self.vel_y = 0
                #check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile.rect.top - self.pos.bottom
                    self.vel_y = 0
                    self.jumped = False

        #update player coordinates
        self.pos.x += dx
        self.pos.y += dy

        for lav in Settings.lava:
            if lav.rect.colliderect(pg.Rect(self.pos.x, self.pos.y, self.rect.width, self.rect.height)):
                self.pos.x = self.startX
                self.pos.y = self.startY
        for spawn in Settings.spawnpoints:
            if not spawn.actived:
                if spawn.rect.colliderect(pg.Rect(self.pos.x, self.pos.y + 2, self.rect.width, self.rect.height)):
                    self.startX = self.pos.x
                    self.startY = self.pos.y
                    spawn.actived = True

        #draw player onto screen
        Settings.screen.blit(self.image, self.rect)
        Settings.playerRect = pg.Rect(self.pos.x, self.pos.y, self.rect.width, self.rect.height)
        #pg.draw.rect(screen, (255, 255, 255), self.pos, 2)