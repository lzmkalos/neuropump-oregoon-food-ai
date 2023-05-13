# Oregon Food - DB Implementation

<img src="./src/neuro_pump.gif">


## 📝 Descripción
<p align="justify">
Aplicación web que permite al personal de Oregon Food registrar sus pedidos de manera eficaz a través de una interfaz intuitiva. Su principal atractivo es optimizar el uso del sistema de base de datos actual a través de una migración desde el Excel existente. La web permite a Oregon Food mantener sus registros, clientes, proveedores para poder ser consultados y actualizados desde cualquier dispositivo: escritorio, móvil y desde la simple comodidad de su casa.
</p>


## 📌 Objetivos principales
### Misión
<p align="justify">
    Ofrecer a los clientes una experiencia de entretenimiento segura y de alta calidad. Nos esforzamos por ofrecer una amplia gama de emocionantes juegos y servicios. Al mismo tiempo que garantizamos altos   estándares de seguridad web y protegemos la seguridad del usuarios con algoritmos encriptación.
</p>


### Visión
<p align="justify">
    Ser reconocidos como el casino virtual lider en el mercado peruano ofreciendo una experiencia de juego única y segura. Nuestro objetivo es favorecer al usuario con ofertas y bonificaciones atractivas y una atención excepcional. Nos esforzamos por estar a la vanguardia en tecnología e innovación de la industria de casinos en línea.
</p>


## 📚 Librerías
- Flask
- UUID
- SQLAlchemy
- WT

## Modelo Relacional de Base de Datos
![]("Oregon Foods - Entidad Relación.png")

## 🚀 Desplegar aplicación
<p align="justify">
    Para correr la aplicación <strong>TumiPalaceApp</strong>, es necesario instalar los módulos de python necesarios. Estos están detallados dentro del archivo requirements.txt, que muestra el nombre del módulo, seguido de su versión. Por otro lado, al usar librerías generadoras de código como <strong>uuid</strong>, es necesario colocar comandos en nuestro postgresql. Para ello hemos detallado la siguiente lista de puntos a considerar:
</p>


1. Crear un ambiente virtual para correr nuestro servidor. Podemos realizarlo a partir de instalar el módulo `pip install virtualenv`. Posteriormente lo creamos con `python3 -m venv env`, siendo `env` el nombre designado.
2. Instalar módulos usando la herramienta pip, seguido de la flag `-r` que apunta a nuestro archivo de requerimientos, `pip install -r requirements.txt`.
3. Acceder a postgresql por terminal mediante el comando: `sudo psql -U postgres`.
4. Crear la tabla de base de datos necesaria, en este caso `tumipalace_db`, utilizando el comando `CREATE DATABASE tumipalace_db;`.
5. Conectarnos a nuestra tabla `\c tumipalace_db;`. Recordar que con `\dt` listamos las relaciones.
6. Correr el programa principal `python3 main.py`.


> Si obtenemos un error parecido a `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`, es por que debemos añadir la siguiente extensión dentro de postgresql (fijarnos que estamos conectados a nuestra tabla): `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`.