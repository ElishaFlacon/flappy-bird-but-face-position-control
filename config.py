import pygame
import pygame.freetype
import src.button.button as btn
import src.characters.bird as bird
import src.database.database as db


# запускаем игру
pygame.init()

# база данных
data = db.Database('data/data.bin')
data.get_data()

# часы
clock = pygame.time.Clock()

# лок на фпс
fps = 30

# название окна
game_caption = "Flappy Bird"
video_caption = "AI"

# размеры окна
screen_width = 864
screen_height = 936

# полезные свойства размера окна
center_of_width = screen_width // 2
center_of_height = screen_height // 2

# картинка кнопки
button_image = pygame.image.load('assets/images/restart.png')

# шрифт
font = pygame.freetype.Font("assets/fonts/main_font.ttf", 48)

# скорость движения объектов
scroll_speed = 5
# нужен, чтобы отслеживать позицию пола
# типо на сколько он передвинулся
ground_scroll = 0

# хз, группы спрайтов или ч?
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

# инициализируем птичку
flappy = bird.Bird(100, center_of_height)
bird_group.add(flappy)

# инициализируем кнопку
button = btn.Button(center_of_width - 50, center_of_height - 100, button_image)

# вертикальное растояние между трубами
pipe_gap = 150
# время в мс через которое появляются новые трубы
pipe_frequency = 2000
# смотрим сколько времени прошло от создания прошлой трубы
last_pipe = pygame.time.get_ticks() - pipe_frequency
# параметр для отслеживания, что птичка прошла сквозь трубы
pass_pipe = False

# экран
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_caption)

# картинки фона
background = pygame.image.load('assets/images/background.png')
ground = pygame.image.load('assets/images/ground.png')

# позиция лица, изначально по центру
face_position = center_of_height

# счет и попытки
score = 0
max_score = data.data.get('max_score')
attempts = data.data.get('attempts')

# состояния игры
flying = False
game_over = False
run = True
