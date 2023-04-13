import pygame


class Pipe(pygame.sprite.Sprite):

    def __init__(self, x, y, position, scroll_speed, pipe_gap):
        pygame.sprite.Sprite.__init__(self)

        self.scroll_speed = scroll_speed

        self.image = pygame.image.load('assets/images/pipe.png')
        # получаем очертания фигуры
        self.rect = self.image.get_rect()

        # растояние между трубами
        self.pipe_gap = pipe_gap

        # если позиция 1, то это верхняя труба, иначе нижняя
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(self.pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(self.pipe_gap / 2)]

    def update(self):
        self.rect.x -= self.scroll_speed

        # уничтожаем трубу, если она вышла за границы экрана
        if self.rect.right < 0:
            self.kill()
