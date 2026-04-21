
Cathedra es una plataforma educativa desarrollada por estudiantes de la Universidad de San Buenaventura, Sede Bogotá, en la Facultad de Ingeniería. Su propósito es reducir la brecha educativa en Colombia, centralizando información sobre becas, programas académicos y oportunidades de financiamiento en un solo espacio digital, accesible e intuitivo.
El proyecto nace como respuesta a una problemática social significativa: según el DANE (2023), menos del 40% de los jóvenes colombianos que culminan la educación media logran acceder a estudios universitarios, en gran parte por la falta de información y las barreras económicas. Cathedra busca cambiar esta realidad.
Este repositorio corresponde al backend y frontend del proyecto, desarrollado con Python (Django), html y css y conectado a una base de datos MySQL.

☁️ En GitHub Codespaces
1. Entra a la carpeta del proyecto
bashcd cathedra_back/cathedra_
2. Instala las dependencias
bashpip install django mysqlclient
3. Corre el servidor
bashpython manage.py runserver
4. Abre la plataforma
Ve a la pestaña "Puertos" en VS Code y abre la URL pública que Codespaces genera. Agrégale /login/ al final:
https://tu-codespace-8000.app.github.dev/login/

🔐 Rutas disponibles
RutaDescripción/login/Iniciar sesión/logout/Cerrar sesión/inicio/Página de inicio/admin/Panel de administración

David Alejandro Malaver,
Nikolas Echeverria,
Nicolas alvarez
