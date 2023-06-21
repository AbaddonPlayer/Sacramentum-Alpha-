import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obs_spr):
        super().__init__(groups)
        self.image = pygame.image.load('GRAPHICS/player/Idle/play3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-5,-24)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attack = False
        self.attack_cd = 400
        self.attack_tm = None

        self.obs_spr = obs_spr

    def input(self):
        keys = pygame.key.get_pressed()

        #MOVEMENT
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        #ATTACK
        if keys[pygame.MOUSEBUTTONDOWN] and not self.attack:
            self.attack = True
            self.attack_tm = pygame.time.get_ticks()
        #MAGIC
        if keys[pygame.K_q] and not self.attack:
            self.attack = True
            self.attack_tm = pygame.time.get_ticks

        if keys[pygame.K_z] and self.can_switch_weapon:
            self.switch_weapon = False
            self.weapon_switch_tm = pygame.time.get_ticks()

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center             

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obs_spr:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #left
                        self.hitbox.left = sprite.hitbox.right    
        
        if direction == 'vertical':
            for sprite in self.obs_spr:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #up
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #down
                        self.hitbox.top = sprite.hitbox.bottom
    
    def update(self):
        self.input()
        self.move(self.speed)