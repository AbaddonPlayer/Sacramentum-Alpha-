import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,spr_typ,surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.spr_typ = spr_typ
        self.image = surface
        if spr_typ == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30,-20)
