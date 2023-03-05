Programa 1: Adoquinamiento.

Para esta práctica se opto por el usar el lenguaje de programación python
y de una biblioteca para la interfaz grafica Tkinter.

Para asegurarse de que cuenta con la biblioteca instalada escribe
el siguiente contacto:

  python3 -m tkinter

En caso de no contar con la biblioteca, ejecutar el siguiente comando
  <gestor> install python3-tk
  gestor := apt | apt-get | pacman | dnf | ...

Se recomienda crear un entorno virtual.
Para las versiones de python superiores a la 3.4:
Para crearlo:
  python3 -m venv <nombre>

Para activarlo:
  source <nombre>/bin/activate

Para desactivarlo:
  deactivate

Para eliminarlo:
  rm -r <nombre>

En caso de que no tengas esta version de python o estés en Windows se recomienda
visitar la siguiente página:
https://python.land/virtual-environments/virtualenv

Una vez el ambiente vitual activado, introduce el siguiente comando para instalar las dependecias:
  pip install -r requirements.txt

Nos movemos a directorio /src para ejecutar el programa escribiendo:
  python main.py <n>
  python3 main.py <n> (En caso de que no se haya creado entorno virtual).

  n := un número natural.
