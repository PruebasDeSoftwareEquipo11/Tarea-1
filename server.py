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
logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipadress = input("Ingrese IP : ")

server_socket.bind((ipadress, port))
server_socket.listen(1)

print("Servidor iniciado en "+str(port))
logging.info(str(datetime.datetime.now())+" Servidor iniciado en "+str(port))

client_socket, client_address = server_socket.accept()
print("Conectado a "+str(client_address))
logging.info(str(datetime.datetime.now())+" Conectado a "+str(client_address))


while True:
    data = client_socket.recv(1024)
    if not data:
        break
    message = data.decode()
    logging.info(str(datetime.datetime.now())+" Mensaje recibido sin decodificar: "+ str(message))
    message = de_codificate(message)
    logging.info(str(datetime.datetime.now())+" Mensaje recibido decodificado: "+ str(message))
    print("Mensaje recibido: "+ str(message))

    
    response = input("Ingrese mensaje : ")
    logging.info(str(datetime.datetime.now())+" Mensaje a enviar: "+ str(message))
    response = de_codificate(response)
    client_socket.sendall(response.encode())
    logging.info(str(datetime.datetime.now())+" Mensaje enviado codificado: "+ str(response))

client_socket.close()
server_socket.close()
logging.info(str(datetime.datetime.now())+" Servidor cerrado")