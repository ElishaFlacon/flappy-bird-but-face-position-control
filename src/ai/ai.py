import cv2


class Ai():
    faceCascade = None
    scale_factor = 0
    face_dots = []
    face_position = 0

    def __init__(self, path_to_cascade, scale_factor=1.2):
        '''
        scale_factor отвечат за увеличение размера входящего кадра от минимального до максимального,
        чем выше значение scale_factor - тем быстрее будет обрабатываться кадр (больше фпс), но качество обработки хуже (может не обнаружить лицо)

        значения scale_factor должно быть от 1 до 1.5, где при 1 будет очень мало фпс, а при 1.5 лицо будет плохо обнаруживаться

        идеальным значением для моей конфигурации пк является 1.2
        '''
        self.scale_factor = scale_factor
        self.faceCascade = cv2.CascadeClassifier(path_to_cascade)

    def processing_frame(self, frame):
        # переводим лицо в серый цвет
        # можно обойтись и без этого
        # но так точнее определяется положение лица
        gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # получаем антропометрические точки
        self.face_dots = self.faceCascade.detectMultiScale(
            gray_face,
            scaleFactor=self.scale_factor,
            minNeighbors=6,
            minSize=(10, 10)
        )

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
