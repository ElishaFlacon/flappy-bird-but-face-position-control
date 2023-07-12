<h1> 
     🐦 Игра Flappy Bird с особым управлением
</h1>

<h3>
Flappy Bird - это та самая культовая игра, но в игре управление птичкой происходит за счет распознавания лица в кадре вебкамеры и вычисление его положения. Игра написана на Python и использует библиотеку PyGame для работы самой игры и библиотеку OpenCV для распознавания лица и вычисления его положения в кадре

</br>
</br>
     
> В игре присутствует шутка майниг ферма, ее можно отключить: удаляем src\fun\mining.py и убраем строки 5 и 8 в main.py
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
- `cd flappy-bird-but-face-position-control`
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

- <a href="https://github.com/ElishaFlacon/flappy-bird-but-face-position-control/assets/83610362/4ffd3ade-f3dc-4187-b3d3-bfed32390d6a">Нажать чтобы демо!</a>
- <video src="https://github.com/ElishaFlacon/flappy-bird-but-face-position-control/assets/83610362/4ffd3ade-f3dc-4187-b3d3-bfed32390d6a" />



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



