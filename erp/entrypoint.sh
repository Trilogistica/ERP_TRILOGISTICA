#!/bin/bash

# Mostrar arte ASCII al inicio
echo "
  ___             _             
 |  __ \           | |            
 | |  | | _   _| | __ _ _ 
 | |  | |/ _ \ / _| |/ / _ | '_| 
 | |_| | () | (_|   |  _| |   
 |__/ \_/ \_||\\_||   
"

# Verifica si `requirements.txt` existe
if [ ! -f requirements.txt ]; then
    echo "❌ requirements.txt no encontrado. Creando un archivo vacío..."
    touch requirements.txt
fi

# Instala dependencias desde requirements.txt
echo -e "\nInstalando dependencias desde requirements.txt..."
pip install --no-cache-dir -r requirements.txt

# Asegúrate de que las dependencias estén sincronizadas cada 5 minutos
function sync_requirements {
    while true; do
        echo -e "\nActualizando requirements.txt con dependencias instaladas..."
        pip freeze > requirements.txt
        echo "✅ requirements.txt actualizado correctamente."
        sleep 300
    done
}

# Ejecutar sincronización de dependencias en segundo plano
sync_requirements &

echo -e "\nIniciando la aplicación..."
exec "$@"

