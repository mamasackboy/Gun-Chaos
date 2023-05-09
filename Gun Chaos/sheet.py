import pygame
import json

class Spritesheet:
    def __init__(self,filename):
        self.filename= filename
        self.sprite_sheet= pygame.image.load(filename).convert()
        
    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite
    def parse_sprite(self,name):
        sprite=self.data["frames"][name]["frame"]
        x,y,w,h = sprite["x"],sprite["y"],sprite["w"],sprite["h"]
        image=self.get_sprite(x,y,w,h)
        return image
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image