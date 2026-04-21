# 🎓 Cathedra — Cómo ejecutar en GitHub Codespaces

### 1. Entra a la carpeta del proyecto

```bash
cd cathedra_back/cathedra_
```

### 2. Instala las dependencias

```bash
pip install django mysqlclient
```

### 3. Corre el servidor

```bash
python manage.py runserver
```

### 4. Abre la plataforma

Ve a la pestaña **"Puertos"** en VS Code y abre la URL pública que Codespaces genera. Agrégale `/login/` al final:

```
https://tu-codespace-8000.app.github.dev/login/
```
