import cv2


class Ai():
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.face_dots = []
        self.face_position = 0

    def processing_face(self, frame):
        # переводим лицо в серый цвет
        # можно обойтись и без этого
        # но так точнее определяется положение лица
        gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # получаем антропометрические точки
        self.face_dots = self.faceCascade.detectMultiScale(gray_face, 1.1, 4)

    def get_face_position(self):
        for (x, y, w, h) in self.face_dots:
            # написать тут чото охото
            self.face_position = ((h // 2 + y) * 2 - 110)

    # рисует квадратную обводку лица
    def show_rectangle(self, frame, color):
        for (x, y, w, h) in self.face_dots:
            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                color,
                2
            )

    # рисует точку по середине лица
    def show_central_dot(self, frame, color):
        for (x, y, w, h) in self.face_dots:
            cv2.rectangle(
                frame,
                (round(x+w/2 + 2), round(y+h/2)),
                (round(x+w/2), round(y+h/2 + 2)),
                color,
                2
            )
