import pygame as pg
import Settings
import GUI
import Block

class World():
    def __init__(self, data):
        self.GUI = GUI.GUI()
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    Settings.tile_list.add(Block.block((col_count * Settings.tile_size, row_count * Settings.tile_size), Settings.Path['dirt_img']))
                elif tile == 2:
                    Settings.tile_list.add(Block.block((col_count * Settings.tile_size, row_count * Settings.tile_size), Settings.Path['grass_img']))
                elif tile == 3:
                    Settings.lava.add(Block.block((col_count * Settings.tile_size, row_count * Settings.tile_size), Settings.Path['lavaUp']))
                elif tile == 4:
                    Settings.spawnpoints.add(Block.spawnpoint((col_count * Settings.tile_size, row_count * Settings.tile_size), Settings.Path['spawpoint']))
                elif tile == 5:
                    Settings.tile_list.add(Block.block((col_count * Settings.tile_size, row_count * Settings.tile_size), Settings.Path['antiBlock']))
                elif tile == 6:
                    Settings.coins.add(Block.item((col_count * Settings.tile_size, row_count * Settings.tile_size), 'img/coin'))
                elif tile == 7:
                    Settings.tile_list.add(Block.slime((col_count * Settings.tile_size, row_count * Settings.tile_size), 'img/slime.png'))
                col_count += 1
            row_count += 1

    def draw(self):
        Settings.tile_list.update()
        for tile in Settings.tile_list:
            Settings.screen.blit(tile.image, pg.Rect(tile.rect.x - Settings.player.pos.x + (Settings.screen_width // 2), tile.rect.y - Settings.player.pos.y + (Settings.screen_width // 2) - ((Settings.screen_width - Settings.screen_height) // 2), tile.rect.w, tile.rect.h))
        for tile in Settings.lava:
            Settings.screen.blit(tile.image, pg.Rect(tile.rect.x - Settings.player.pos.x + (Settings.screen_width // 2), tile.rect.y - Settings.player.pos.y + (Settings.screen_width // 2) - ((Settings.screen_width - Settings.screen_height) // 2), tile.rect.w, tile.rect.h))
        for tile in Settings.spawnpoints:
            Settings.screen.blit(tile.image, pg.Rect(tile.rect.x - Settings.player.pos.x + (Settings.screen_width // 2), tile.rect.y - Settings.player.pos.y + (Settings.screen_width // 2) - ((Settings.screen_width - Settings.screen_height) // 2), tile.rect.w, tile.rect.h))
        Settings.coins.update()
        for tile in Settings.coins:
            Settings.screen.blit(tile.image, pg.Rect(tile.rect.x - Settings.player.pos.x + (Settings.screen_width // 2), tile.rect.y - Settings.player.pos.y + (Settings.screen_width // 2) - ((Settings.screen_width - Settings.screen_height) // 2), tile.rect.w, tile.rect.h))
            #pg.draw.rect(screen, (255, 255, 255), tile[1], 2)
        #print((Settings.screen_width // 2 - 5))
        self.GUI.update()