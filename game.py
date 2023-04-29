import random
import pygame
import pygame.freetype
import src.props.pipe as pipe
import src.button.button as button
import src.characters.bird as bird


pygame.init()


class Game():
    clock = pygame.time.Clock()

    # название окон
    game_caption = "Flappy Bird"
    video_caption = "AI"

    # картинка кнопки
    button_image = pygame.image.load('assets/images/restart.png')

    # шрифт
    font = pygame.freetype.Font("assets/fonts/main_font.ttf", 48)

    # это просто не трогать!
    ground_scroll = 0

    # хз, группы спрайтов или ч?
    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()

    # время в мс через которое появляются новые трубы
    pipe_frequency = 1000

    # смотрим сколько времени прошло от создания прошлой трубы
    last_pipe = pygame.time.get_ticks() - pipe_frequency

    # параметр для отслеживания, что птичка прошла сквозь трубы
    pass_pipe = False

    # картинки фона
    background = pygame.image.load('assets/images/background.png')
    ground = pygame.image.load('assets/images/ground.png')

    # счет
    score = 0

    # состояния игры
    flying = False
    game_over = False
    run = True

    def __init__(self, fps, database, scroll_speed=5, screen_size=(864, 936)):
        pygame.init()
        random.seed()
        self.fps = fps

        # всякие свойства окна
        self.screen_width, self.screen_height = screen_size
        self.center_of_width = self.screen_width // 2
        self.center_of_height = self.screen_height // 2

        # создаем окно
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption(self.game_caption)

        # "база данных"
        self.database = database

        # получаем максимальный счет и попытки
        self.max_score = database.data.get('max_score')
        self.attempts = database.data.get('attempts')

        # получаем изначальное положение для птички
        self.face_position = self.center_of_height

        # скорость полета птички
        self.scroll_speed = scroll_speed

        # инициализируем птичку
        self.flappy = bird.Bird(100, self.center_of_height)
        self.bird_group.add(self.flappy)

        # инициализируем кнопку
        self.button = button.Button(
            self.center_of_width - 50,
            self.center_of_height - 100,
            self.button_image
        )

    def pipe_gap(self):
        return random.randint(140, 220)

    def feetch_data(self):
        self.database.get_data()
        self.max_score = self.database.data.get('max_score')
        self.attempts = self.database.data.get('attempts')

    def font_render(self, text, x, y, color, screen, size):
        self.font.render_to(
            screen,
            (x, y),
            text,
            color,
            size=size
        )

    def play(self, face_position, camera):
        self.clock.tick(self.fps)

        # считаем расстояние между трубами в зависимости от фпс
        # иначе при низком фпс трубы спавняться вплотную
        self.pipe_frequency = int(800 / (self.clock.get_fps()/100 + 0.01))

        # отрисовываем фон
        self.screen.blit(self.background, (0, 0))

        # отрисовываем птичку
        self.bird_group.draw(self.screen)
        self.bird_group.update(
            face_position, self.flying, self.game_over)

        # отрисовываем трубы
        self.pipe_group.draw(self.screen)

        # отрисовываем нижний фон, это нужно чтобы трубы уходили за него
        self.screen.blit(self.ground, (self.ground_scroll, 768))

        # обрабатываем пролет труб
        if len(self.pipe_group) > 0:
            if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.left\
                    and self.bird_group.sprites()[0].rect.right < self.pipe_group.sprites()[0].rect.right\
                    and self.pass_pipe == False:
                self.pass_pipe = True

            if self.pass_pipe == True:
                if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.right:
                    self.score += 1
                    self.pass_pipe = False

        # обрабатываем удар об трубу
        if pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False):
            self.game_over = True

        # играем, если не проиграли))
        if self.game_over == False and self.flying == True:
            time_now = pygame.time.get_ticks()

            # логика создания труб
            if time_now - self.last_pipe > self.pipe_frequency:
                pipe_height = random.randint(-350, 150)

                # создаем верхнюю и нижнюю трубу
                top_pipe = pipe.Pipe(
                    self.screen_width,
                    ((self.center_of_height) + pipe_height),
                    1,
                    self.scroll_speed,
                    self.pipe_gap()
                )
                bottom_pipe = pipe.Pipe(
                    self.screen_width,
                    ((self.center_of_height) + pipe_height),
                    -1,
                    self.scroll_speed,
                    self.pipe_gap()
                )

                self.pipe_group.add(bottom_pipe)
                self.pipe_group.add(top_pipe)

                self.last_pipe = time_now

            # логика передвежения пола
            self.ground_scroll -= self.scroll_speed
            if abs(self.ground_scroll) > 35:
                self.ground_scroll = 0

            # обновляем положение труб
            # делаем это здесь, чтобы при проигрыше
            # трубы останавливаись
            self.pipe_group.update()

        # проверяем на проигрыш и перезапускаем игру
        if self.game_over == True:
            if self.button.draw(self.screen) == True:
                # теперь не гейм овер
                self.game_over = False

                # записываем данные, в которых увеличиваем количество попыток
                self.database.update_data(self.max_score, self.attempts + 1)

                # если побили рекод, то записываем данные с новым рекордом
                # и увеличиваем количество попыток
                if self.score > self.max_score:
                    self.database.update_data(self.score, self.attempts + 1)

                # записываем данные
                self.database.post_data()

                # перезапускаем игру
                self.reset()

        # тут обрабатываем всякие события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                camera.close_camera()
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN and self.flying == False and self.game_over == False:
                self.flying = True

        # тут рендерим текст
        self.font_render(
            str(self.score),
            self.center_of_width,
            850,
            (255, 255, 255),
            self.screen,
            64
        )
        self.font_render(
            f'Попыток: {self.attempts}',
            10,
            875,
            (255, 255, 255),
            self.screen,
            18
        )
        self.font_render(
            f'Лучший счет: {self.max_score}',
            10,
            900,
            (255, 255, 255),
            self.screen,
            18
        )
        self.font_render(
            f'FPS:{self.clock.get_fps():2.0f}',
            10,
            825,
            (255, 255, 255),
            self.screen,
            18
        )

        pygame.display.update()

    def reset(self):
        # удаляем трубы
        self.pipe_group.empty()

        # ставим птичку в изначальную позицию
        self.flappy.rect.x = 100
        self.flappy.rect.y = self.center_of_height

        # очищаем счет
        self.score = 0

        # получаем актуальные значения
        self.feetch_data()

    def close(self):
        # не пытайся покинуть Саратов...
        pygame.quit()
