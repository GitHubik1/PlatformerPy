import pygame as pg
import WorldData
import World
import Player

clock = pg.time.Clock()
fps = 60

screen_width = 1000
screen_height = 800

screen = pg.display.set_mode((screen_width, screen_height), pg.SCALED)
pg.display.set_caption('Platformer')

#define game variables
tile_size = 50
score = 0

JUMPPOWER = 16
GRAVITY = 0.8
SPEED = 10

#load images
Images = {
    'sun_image': pg.image.load('img/sun.png'),
    'background_image': pg.image.load('img/sky.png'),
    'dirt_img': pg.image.load('img/dirt.png'),
    'grass_img': pg.image.load('img/grass.png')
}

Path = {
    'sun_image': 'img/sun.png',
    'background_image': 'img/sky.png',
    'dirt_img': 'img/dirt.png',
    'grass_img': 'img/grass.png',
    'lavaUp': 'img/lavaUp.png',
    'spawpoint': 'img/gold_block.png',
    'antiBlock': 'img/antiBlock.png',
    'diamond': 'img/coin/diamond1.png',
}

Fonts = {
    'counterFont': pg.font.Font('font/Main.ttf', tile_size) ,
}

tile_list = pg.sprite.Group()
lava = pg.sprite.Group()
spawnpoints = pg.sprite.Group()
coins = pg.sprite.Group()

player = Player.Player(screen_width // 2, screen_height // 2)
playerRect = player.rect
world = World.World(WorldData.world_data)