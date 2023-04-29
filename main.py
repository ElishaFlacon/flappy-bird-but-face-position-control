import game
import config
import src.ai.ai as ai
import src.camera.camera as cam


recognizer = ai.Ai('src/ai/haarcascade_frontalface_default.xml')
camera = cam.Camera()
game = game.Game(
    config.fps,
    config.data,
    screen_size=config.screen_size
)


def main():
    while (game.run):
        # читаем кадры с камеры
        camera.read()

        # обрабатываем кадры
        recognizer.processing_frame(camera.frame)

        # получаем позицию лица
        recognizer.get_face_position()

        # отрисовываем контуры лица
        recognizer.show_rectangle(camera.frame, (0, 255, 0))
        recognizer.show_central_dot(camera.frame, (0, 0, 255))

        # выводим на экран
        camera.show(config.video_caption)

        # обрабатываем игру
        game.play(recognizer.face_position, camera)


if __name__ == '__main__':
    main()

game.close()
