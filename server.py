import socket
import subprocess

# Configura el host y el puerto en el que se va a escuchar
host = '0.0.0.0'  # Escucha en todas las interfaces de red
port = 12345

# Crea un socket y enlázalo al host y puerto
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print('Esperando conexiones...')

# Acepta la conexión entrante
client_socket, client_address = server_socket.accept()
print('Conexión establecida desde:', client_address)

# Captura el audio del micrófono y envíalo al cliente
subprocess.run(['termux-microphone-record', '-f', 'output.wav'])
with open('output.wav', 'rb') as audio_file:
    audio_data = audio_file.read()
client_socket.sendall(audio_data)

# Cierra los sockets y elimina el archivo de audio temporal
client_socket.close()
server_socket.close()
subprocess.run(['rm', 'output.wav'])
