import pygame
from settings import *
from tile import  Tile
from player import Player
from debug import debug
from support import *
from random import choice

class Level:
    def __init__(self):
        
        self.dis_srf = pygame.display.get_surface()

        self.vis_spr = Ycamgroup()
        self.obs_spr = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        layout = {
            'boundary': import_csv_layout('DATA/PortobelloBrook_Walls.csv'),
            'mushroom': import_csv_layout('DATA/PortobelloBrook_Mushrooms.csv'),
            'object': import_csv_layout('DATA/PortobelloBrook_Objects.csv')
        }
        graphics = {
            'mushroom': import_folder('GRAPHICS/mushroom'),
            'object': import_folder('GRAPHICS/objects')
        }       

        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                    if style == 'boundary':
                        Tile ((x,y),[self.obs_spr],'invisible')
                    if style == 'mushroom':
                        pass
                        #rnd_msh_img = choice(graphics['mushroom'])
                        #Tile((x,y),[self.vis_spr,self.obs_spr],'mushroom',rnd_msh_img)
                    if style == 'object':
                        pass
                        #srf = graphics['object'][int(col)]
                        #Tile((x,y),[self.vis_spr,self.obs_spr],'object',srf)

        self.player = Player((480,96),[self.vis_spr],self.obs_spr)

   
    def run(self):
        self.vis_spr.custom_draw(self.player)
        self.vis_spr.update()
        self.ui.display(self.player)

    def run(self):
        self.vis_spr.custom_draw(self.player)
        self.vis_spr.update()

class Ycamgroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.dis_srf = pygame.display.get_surface()
        self.half_width = self.dis_srf.get_size()[0] // 2
        self.half_height = self.dis_srf.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_srf = pygame.image.load('TILED/PortobelloBrook.png').convert()
        self.floor_rct = self.floor_srf.get_rect(topleft = (0,0))

    def custom_draw(self,player):
        
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_off_pos = self.floor_rct.topleft - self.offset
        self.dis_srf.blit(self.floor_srf,floor_off_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            off_pos = sprite.rect.topleft - self.offset
            self.dis_srf.blit(sprite.image,off_pos)
    
    