# ERP_TRILOGISTICA

- Clonar este repositorio
- Crear un usuario en postgres.
- Crear una venv
 ```bash
   python -m venv mienviroment
```
- Luego instala las dependencias
 ```bash
  pip install setuptools wheel
```
 ```bash
  pip install -r requirements.txt
```
- Ahora crea una base de datos local en postgres
- Crea tu modulo en la carpeta modulos_desarrollados
 ```bash
  Python odoo-bin scaffold “modulo_nombre” modulos_desarrollados
```
- Ahora inicia el proyecto
 ```bash
  python odoo-bin -r usuario -w password --addons-path=addons,modulos_desarrollados -d base_de_datos -i base
```
