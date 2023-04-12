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


port = 12345
logging.basicConfig(filename='client.log', encoding='utf-8', level=logging.DEBUG)
tipodeIP = input("Ingrese tipo de IP a ingresar (1 = IPv4, 2 = IPv6) : ")
ipadress = input("Ingrese IP a conectar : ")

server_address = (ipadress, port)
if tipodeIP == "2":
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
else:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    client_socket.connect(server_address)
except:
    print("No se pudo conectar")
    logging.warning("No se pudo conectar")
logging.info(str(datetime.datetime.now())+" Conectado a servidor "+str(server_address))

while True:
    message = input("Ingrese mensaje : ")
    logging.info(str(datetime.datetime.now())+" Mensaje a enviar : "+str(message))
    message = de_codificate(message)
    try:
        client_socket.sendall(message.encode())
    except:
        print("No se pudo enviar")
        logging.warning("No se pudo enviar")
    logging.info(str(datetime.datetime.now())+" Mensaje codificado enviado : "+str(message))
    try:
        data = client_socket.recv(1024)
    except:
        print("No se pudo recibir")
        logging.warning("No se pudo recibir")
    if not data:
        break
    response = data.decode()
    logging.info(str(datetime.datetime.now())+" Mensaje sin decodificar : "+str(response))
    response = de_codificate(response)
    print("Mensaje recibido : "+str(response))
    logging.info(str(datetime.datetime.now())+" Mensaje recibido : "+str(response))

client_socket.close()
logging.info(str(datetime.datetime.now())+" Conexion finalizada")