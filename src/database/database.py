class Database():
    def __init__(self, path):
        self.path = path
        self.data = {
            'attempts': 0,
            'max_score': 0,
        }

    def get_data(self):
        file = open(self.path, 'rb')
        bytes_strings = file.readlines()

        # если true - ключ, если false - значение
        current = True

        for item in bytes_strings:
            if current:
                # [:-1] чтобы убрать \n
                key = item.decode()[:-1]

                current = False

            else:
                value = int(item.decode()[:-1])
                self.data[key] = value

                current = True
        file.close()

    def post_data(self):
        file = open(self.path, 'wb')

        for key in self.data:
            value = self.data[key]

            value = str(value) + '\n'
            key = key + '\n'

            # конвертируем
            bytes_key = key.encode()
            bytes_value = value.encode()

            # запись
            file.write(bytes_key)
            file.write(bytes_value)
        file.close()

    def update_data(self, max_score, attempts):
        self.data = {
            'attempts': attempts,
            'max_score': max_score,
        }

        # после обновления значений сразу записываем их
        # self.post_data()
