import pygame


class Sprites:
    def __init__(self, pos, size, texture):
        self.pos = pygame.rect.Rect(*pos, *size)
        self.size = size
        self.texture = pygame.image.load(texture)

    def tick(self, **kwargs):
        pass

    def display(self):
        return self.texture

    def render(self, display):
        display.blit(self.display(), self.pos)
