import pygame


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        mouse_position = pygame.mouse.get_pos()
        action = False

        # если мышка на кнопке
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                action = True

        # открисовка кнопки
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
