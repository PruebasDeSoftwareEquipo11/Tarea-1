import logging
import datetime
import socket

def de_codificate(mensaje):
    # Algoritmo de codificacion utilizando XOR Cyphering

    xorKey = 'C'
    largomensaje = len(mensaje)
    for i in range(largomensaje):
        mensaje = (mensaje[:i] + chr(ord(mensaje[i]) ^ ord(xorKey)) + mensaje[i + 1:])
    
    return mensaje

port = 10500
logging.basicConfig(filename='client.log', encoding='utf-8', level=logging.DEBUG)
ipadress = input("Ingrese IP a conectar : ")

server_address = (ipadress, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
logging.info(str(datetime.datetime.now())+" Conectado a servidor "+str(server_address))

while True:
    message = input("Ingrese mensaje : ")
    logging.info(str(datetime.datetime.now())+" Mensaje a enviar : "+str(message))
    message = de_codificate(message)
    client_socket.sendall(message.encode())
    logging.info(str(datetime.datetime.now())+" Mensaje codificado enviado : "+str(message))
    data = client_socket.recv(1024)
    if not data:
        break
    response = data.decode()
    logging.info(str(datetime.datetime.now())+" Mensaje sin decodificar : "+str(response))
    response = de_codificate(response)
    print("Mensaje recibido : "+str(response))
    logging.info(str(datetime.datetime.now())+" Mensaje recibido : "+str(response))

client_socket.close()
logging.info(str(datetime.datetime.now())+" Conexion finalizada")