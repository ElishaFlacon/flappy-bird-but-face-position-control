import pygame


class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.index = 0
        self.counter = 0

        # загружаем кадры анимации птики
        for image_index in range(1, 4):
            image = pygame.image.load(f'assets/images/bird{image_index}.png')
            self.images.append(image)
        self.image = self.images[self.index]

        # получаем очертания птички
        self.rect = self.image.get_rect()
        # центрируем птичку по координатам
        self.rect.center = [x, y]

    # принимает позицию лица, состояние flying и состояние game_over
    def update(self, face_position, flying, game_over):
        if flying and game_over == False:
            if (face_position > 0 and face_position < 730):
                self.rect.y = face_position

        if game_over == False:
            self.counter += 1
            flap_cooldown = 3

            # задержка перед следующим кадром
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1

            # когда дошли до последнего кадра переходим на первый
            if self.index > 2:
                self.index = 0

            # получаем нужный кадр
            self.image = self.images[self.index]

            # меняю поворт птички, взависимости от ее расположения
            self.image = pygame.transform.rotate(
                self.images[self.index],
                ((face_position - 365) // 73 * 3)
            )

        if game_over == True:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
