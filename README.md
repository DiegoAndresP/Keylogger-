# 🖥️ Keylogger Cliente-Servidor

Sistema de captura remota de pulsaciones de teclado a través de una arquitectura cliente-servidor. El cliente registra las teclas oprimidas y las transmite a un servidor remoto mediante sockets TCP, donde se almacenan con marca de tiempo en archivos de texto.

> ❗ Este proyecto está diseñado para prácticas técnicas y experimentación en entornos controlados.

---

## 📂 Estructura del Proyecto

Keylogger/ ├── host-keylogger/ │ └── key.py # Script cliente que captura y envía las teclas ├── serv-keylogger/ │ └── serv-keylogger.py # Script servidor que recibe y guarda las pulsaciones



## ⚙️ Requisitos

### Cliente (Windows)

- Python 3.x instalado
- Módulo `pynput` instalado:
  ```bash
  pip install pynput
Servidor (Kali Linux)
Python 3.x instalado (viene por defecto)

Permisos para abrir puertos TCP

Acceso a red local

🚀 Configuración y Ejecución


🔹 1. Configurar y ejecutar el servidor (en Kali Linux)

Abre serv-keylogger.py

Cambia esta línea si quieres usar una IP específica:

host = '0.0.0.0'  # Escucha en todas las interfaces

port = 5000

Corre el servidor:

bash:
python3 serv-keylogger.py

✅ El script empezará a escuchar y mostrará:
[+] Esperando conexión en 0.0.0.0:5000...

🔹 2. Configurar y ejecutar el cliente (en Windows)

Abre key.py

Edita esta línea con la IP real de Kali Linux:

host_ip = "192.168.X.X"  # IP del servidor (Kali)

Corre el cliente:

python key.py

🔹 3. Detener el proceso
Presiona la tecla Esc en el equipo cliente

El programa cerrará la conexión y finalizará la escritura del archivo de registro en el servidor

📝 Salida del servidor

Cada ejecución del servidor genera un archivo de texto en el mismo directorio con el siguiente formato:

keylog_2025-04-24_20h-43m-17s.txt

Cada línea representa una pulsación capturada, por ejemplo:

[2025-04-24 20:44:01] Tecla presionada: h

[2025-04-24 20:44:01] Tecla presionada: o

[2025-04-24 20:44:01] Tecla especial presionada: Key.space


🧩 Posibles Errores y Soluciones

OSError: [Errno 98] Address already in use	El puerto ya está en uso	Matar el proceso o usar otro puerto

ConnectionRefusedError	El servidor no está corriendo	Iniciar serv-keylogger.py en Kali

No se capturan letras en Kali	key.py no tiene permisos o falta pynput	Ejecutar con sudo y verificar el módulo

El log no se llena en el servidor	IP mal configurada en el cliente	Revisar IP de host_ip

🔐 Seguridad y Responsabilidad
Este código es funcional y operativo. Su uso fuera de un entorno controlado o con fines no autorizados es responsabilidad total del usuario.

