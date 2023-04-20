<h1> 
     🐦 Культовая игра Flappy Bird, но управление с помощью лица в кадре
</h1>

<h3>
Управление птичкой в игре происходит за счет разпознования лица в кадре вебкамеры и вычисление его положения
</h3>


</br>



<h2>
  🛠️ Библиотеки для работы игры:
</h2>

- pygame==2.3.0
- deepface==0.0.75
- opencv-python==4.6.0.66
- tensorflow==2.2.0



</br>



<h2>
  🚀 Зпуск игры:
</h2>

- git clone https://github.com/ElishaFlacon/flappy-bird-but-face-position-control.git
- cd flappy-bird-but-face-position-control
- python -m venv <venv_name>
- source <venv_name>/Scripts/activate (linux) or <venv_name>/Scripts/activate (windows)
- pip install -r ./requirements.txt
- в зависимости от разрешения камеры играемся с формулой (src/ai/ai.py/get_face_position()), которая расчитывает как сдвинуть птичку при изменении положения лица в кадре 
- изменяем остальной код под свои нужды
- python main.py
- или скачиваем релиз или ветку build и в папке dist запускаем main.exe
<h3>
    Запускаем, не работет, ура! 🗿🚬
</h3>


</br>



<h2>
 📺 Демо:
</h2>

<p align="center">
  <video src="https://user-images.githubusercontent.com/83610362/231952457-775c2fae-ed60-47f4-b3c9-97c64f4171b7.mp4" controls align="center"/>
</p>

</br>



<h2>
⚡ Немного дополнительной информации:
</h2>

- При создании проекта использовалась вебкамера A4Tech PK-336E (640x480 30fps)
- Проект разрабатывался на ведре с характеристиками i7-3770, gtx 980, 8gb ddr3
- Для стабильной работы игры - кадр должен быть хорошо освещен, а фон должен быть светлым, так же, в идеале, одежда человека в кадре не должна быть темного цвета, иначе будут просадки фпс (возможно в будущем пофикшу)
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



