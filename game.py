import pygame
import random
import config
import src.props.pipe as pipe


'''

да там много слова конфиг и всякое такое
и вообще это все можно красиво разбить на класс game
и в нем сделать кучу методов
код был бы чище, читабельнее и всякое такое
но не сегодня, да и наверно никогда)) 

'''


random.seed()


def feetch_data():
    config.data.get_data()
    config.max_score = config.data.data.get('max_score')
    config.attempts = config.data.data.get('attempts')


def close_game():
    # не пытайся покинуть Саратов...
    pygame.quit()


def reset_game():
    # удаляем трубы
    config.pipe_group.empty()

    # ставим птичку в изначальную позицию
    config.flappy.rect.x = 100
    config.flappy.rect.y = config.center_of_height

    # очищаем счет
    config.score = 0

    # получаем актуальные значения
    feetch_data()


def font_render(text, x, y, color, screen, size):
    config.font.render_to(
        screen,
        (x, y),
        text,
        color,
        size=size
    )


def game(face_position, camera):
    config.clock.tick(config.fps)

    # считаем горизонтальное расстояние между трубами в зависимости от фпс
    # иначе при низком фпс трубы спавняться вплотную
    config.pipe_frequency = int(800 / (config.clock.get_fps()/100 + 0.01))

    # отрисовываем фон
    config.screen.blit(config.background, (0, 0))

    # отрисовываем птичку
    config.bird_group.draw(config.screen)
    config.bird_group.update(face_position, config.flying, config.game_over)

    # отрисовываем трубы
    config.pipe_group.draw(config.screen)

    # отрисовываем нижний фон, это нужно чтобы трубы уходили за него
    config.screen.blit(config.ground, (config.ground_scroll, 768))

    # обрабатываем пролет труб
    if len(config.pipe_group) > 0:
        if config.bird_group.sprites()[0].rect.left > config.pipe_group.sprites()[0].rect.left\
                and config.bird_group.sprites()[0].rect.right < config.pipe_group.sprites()[0].rect.right\
                and config.pass_pipe == False:
            config.pass_pipe = True

        if config.pass_pipe == True:
            if config.bird_group.sprites()[0].rect.left > config.pipe_group.sprites()[0].rect.right:
                config.score += 1
                config.pass_pipe = False

    # обрабатываем удар об трубу
    if pygame.sprite.groupcollide(config.bird_group, config.pipe_group, False, False):
        config.game_over = True

    # играем, если не проиграли))
    if config.game_over == False and config.flying == True:
        time_now = pygame.time.get_ticks()

        # логика создания труб
        if time_now - config.last_pipe > config.pipe_frequency:
            pipe_height = random.randint(-350, 150)

            # создаем верхнюю и нижнюю трубу
            top_pipe = pipe.Pipe(
                config.screen_width,
                ((config.center_of_height) + pipe_height),
                1,
                config.scroll_speed,
                random.randint(140, 220)
            )
            bottom_pipe = pipe.Pipe(
                config.screen_width,
                ((config.center_of_height) + pipe_height),
                -1,
                config.scroll_speed,
                random.randint(140, 220)
            )

            config.pipe_group.add(bottom_pipe)
            config.pipe_group.add(top_pipe)

            config.last_pipe = time_now

        # логика передвежения пола
        config.ground_scroll -= config.scroll_speed
        if abs(config.ground_scroll) > 35:
            config.ground_scroll = 0

        # обновляем положение труб
        # делаем это здесь, чтобы при проигрыше
        # трубы останавливаись
        config.pipe_group.update()

    # проверяем на проигрыш и перезапускаем игру
    if config.game_over == True:
        if config.button.draw() == True:
            # теперь не гейм овер
            config.game_over = False

            # записываем данные, в которых увеличиваем количество попыток
            config.data.update_data(config.max_score, config.attempts + 1)

            # если побили рекод, то записываем данные с новым рекордом
            # и увеличиваем количество попыток
            if config.score > config.max_score:
                config.data.update_data(config.score, config.attempts + 1)

            # записываем данные
            config.data.post_data()

            # перезапускаем игру
            reset_game()

    # тут обрабатываем всякие события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            camera.close_camera()
            config.run = False
        if event.type == pygame.MOUSEBUTTONDOWN and config.flying == False and config.game_over == False:
            config.flying = True

    # тут рендерим текст
    font_render(
        str(config.score),
        config.center_of_width,
        850,
        (255, 255, 255),
        config.screen,
        64
    )
    font_render(
        f'Попыток: {config.attempts}',
        10,
        875,
        (255, 255, 255),
        config.screen,
        18
    )
    font_render(
        f'Лучший счет: {config.max_score}',
        10,
        900,
        (255, 255, 255),
        config.screen,
        18
    )
    font_render(
        f'FPS:{config.clock.get_fps():2.0f}',
        10,
        825,
        (255, 255, 255),
        config.screen,
        18
    )

    pygame.display.update()
