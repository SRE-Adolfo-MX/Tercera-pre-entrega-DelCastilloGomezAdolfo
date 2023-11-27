# Tercera-pre-entrega-DelCastilloGomezAdolfo

Este es la tercera entrega del curso Python en CoderHouse!

> Autor:
- Alumno: Adolfo Del Castillo Gomez

## Configuracion previa instalacion de software.

- Python version: Python 3.11.6
- sqlite version: SQLite 3.0
- django version: django 4.2.7


## Crear la DB y crear arquitectura de DB.

En la consolo ejecutaremos los siguientes comandos para incializar la DB y crear la estructura:

En la carpeta /tercer_proyecto/ buscamos el archivo manage.py

    $ python3 manage.py makemigrations
    $ python3 manage.py migrations
    >>>

Una vez ejecutado los comandos se creara el archivo db.sqlite3 donde tendremos nuestra DB.

## Inicializar servidor web.

En la consola de tu equipo ejecuta el siguiente comando:

    $ python3 manage.py runserver
    >>>

Una vez ejecutado entraras a la siguiente URL desde algun browser en tu equipo donde esta corriento tu servicio web:

- http://127.0.0.1:8000/

## Sitio Web.

Una vez en el sitio podremos ver que en la raiz tenemos dos apartados:

- admin/
- app/

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen1.png</span><span>)</span>

En este caso usaremos el apartado app/ quedando la URL de esta manera:

- http://127.0.0.1:8000/app/

Una vez dentro podremos ver varios apartados:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen2.png</span><span>)</span>


El que nos intereza es show/, quedando la URL de la siguiente manera:

- http://127.0.0.1:8000/app/show/

El sitio creado se visualizara de la siguiente manera:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen3.png</span><span>)</span>

Para incializar comenzaremos con la seccion de publicar:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen4.png</span><span>)</span>

Aqui veremos el siguiente formulario el cual agregaremos los datos y le daremos crear:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen5.png</span><span>)</span>

Despues de ello nos iremos a la seccion de Publicaciones y veremos lo siguiente:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen6.png</span><span>)</span>

Una lista de varios comentarios de los usuarios:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen7.png</span><span>)</span>

En la parte superior podemos filtrar los comentarios por usuario si es que tuvieramos muchos comentarios, asi que aqui fitramos en el campo de texto el id del usuario que queremos revisar que es carlos2023 y damos clic en el boton de buscar y solo veremos el comentario del usuario:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen8.png</span><span>)</span>

Si queremos ver la seccion de usuarios solo seleccionamos esta misma en la barra:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen9.png</span><span>)</span>

Al entrar a esta seccion veremos la lista de usuarios y tambien esta misma podemos filtrar por el ID del usuario y revisar sus datos como nombre completo y email:

<span>https://github.com/SRE-Adolfo-MX/Tercera-pre-entrega-DelCastilloGomezAdolfo/tree/master/tercer_proyecto/git_images/imagen10.png</span><span>)</span>

