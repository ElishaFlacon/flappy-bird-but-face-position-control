<h1> 
     🐦 Игра Flappy Bird с особым управлением
</h1>

<h3>
В игре управление птичкой происходит за счет разпознования лица в кадре вебкамеры и вычисление его положения. Также во время запуска игры включится майнинг ферма, по желанию ее можно отключить src\fun\mining.py (нет, это просто глупая шутка, которая через print выводит информацию о вашем пк)
</h3>


</br>



<h2>
  🛠️ Инструменты, которые использовались при разработке игры:
</h2>

- Python
- OpenCV
- Pygame



</br>



<h2>
  🚀 Зпуск игры:
</h2>

- `git clone https://github.com/ElishaFlacon/flappy-bird-but-face-position-control.git`
-` cd flappy-bird-but-face-position-control`
- `python -m venv <venv_name>`
- `<venv_name>/Scripts/activate` (windows) или `source <venv_name>/Scripts/activate` (linux)
- `pip install -r ./requirements.txt`
- в зависимости от разрешения камеры играемся с формулой (src/ai/ai.py/get_face_position()), которая расчитывает как сдвинуть птичку при изменении положения лица в кадре 
- изменяем остальной код под свои нужды
- модуль fun по желанию можно удалить
- `python main.py`
- или скачиваем релиз или ветку build и в папке dist запускаем main.exe
<h3>
    Запускаем, не работет, ура! 🗿🚬
</h3>


</br>



<h2>
 📺 Демо:
</h2>

- <a href="https://github-production-user-asset-6210df.s3.amazonaws.com/83610362/231952457-775c2fae-ed60-47f4-b3c9-97c64f4171b7.mp4">Нажать чтобы демо!</a>

<p align="center">
     <video src="https://github-production-user-asset-6210df.s3.amazonaws.com/83610362/231952457-775c2fae-ed60-47f4-b3c9-97c64f4171b7.mp4" alt="А ГДЕ? ТУТ ДОЛЖНО БЫТЬ ВИДЕО!" controls align="center" />
</p>



</br>



<h2>
⚡ Немного дополнительной информации:
</h2>

- На данный момент проект полностью реализован!
- При создании проекта использовалась вебкамера A4Tech PK-336E (640x480 30fps)
- Проект разрабатывался на ведре с характеристиками i7-3770, gtx 980, 8gb ddr3
- Для стабильной работы игры - кадр должен быть хорошо освещен, а фон должен быть светлым, так же, в идеале, одежда человека в кадре не должна быть темного цвета, иначе будут просадки фпс
- P.S. Все баги и недочеты - это фичи



<br/>
<br/>
<br/>
<br/>
<br/>
<br/>



<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=d179b8&height=64&section=footer"/>
</p>



