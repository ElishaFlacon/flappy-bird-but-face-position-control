import cv2


class Camera():
    def __init__(self):
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # если первая камера не открылась, открываем другую
        # если камера так и не открылась, то измените первый агрумент
        # метода VideoCapture на единицу больше
        # если это не решило проблему, проверьте системные настройки
        if not self.camera.isOpened():
            self.camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

        self.frame = []

    def read(self):
        # читаем кадры с вебки
        self.frame = self.camera.read()[1]

    def show(self, caption):
        cv2.imshow(caption, self.frame)

    def close_camera(self):
        self.camera.release()
        cv2.destroyAllWindows()
