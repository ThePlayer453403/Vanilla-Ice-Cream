import pygame
from vanilla_api.sprites.sprites import Sprites
from vanilla_api.emoji.emoji import *


class Button(Sprites):
    def __init__(self, pos, size, texture, texture_hover, texture_pressed, command):
        super().__init__(pos, size, texture)
        self.texture_hover = pygame.image.load(texture_hover)
        self.texture_pressed = pygame.image.load(texture_pressed)
        self.state = ""
        self.clicked = command

    def tick(self, mouse, **kwargs):
        if self.pos.collidepoint(mouse[0]):
            if mouse[1][0]:
                if self.state != "pressed":
                    self.clicked()
                self.state = "pressed"
            else:
                self.state = "hover"
        else:
            self.state = ""

    def display(self):
        if self.state == "":
            return self.texture
        if self.state == "pressed":
            return self.texture_pressed
        if self.state == "hover":
            return self.texture_hover
