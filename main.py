import game
import config
import src.ai.ai as ai
import src.camera.camera as cam


recognizer = ai.Ai()
camera = cam.Camera()


def main():
    while (config.run):
        # читаем кадры с камеры
        camera.read()

        # обрабатываем кадры
        recognizer.processing_face(camera.frame)

        # получаем позицию лица
        recognizer.get_face_position()

        # отрисовываем контуры лица
        recognizer.show_rectangle(camera.frame, (0, 255, 0))
        recognizer.show_central_dot(camera.frame, (0, 0, 255))

        # выводим на экран
        camera.show(config.video_caption)

        # обрабатываем игру
        game.game(recognizer.face_position, camera)


# иф наме равно майн то бла бла бла
if __name__ == '__main__':
    main()


# офаем
game.close_game()
