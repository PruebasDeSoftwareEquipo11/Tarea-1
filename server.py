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
logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG)



tipodeIP = input("Ingrese tipo de IP a ingresar (1 = IPv4, 2 = IPv6) : ")

if tipodeIP == "2":
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
else:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipadress = input("Ingrese IP : ")

try:
    server_socket.bind((ipadress, port))
except:    
    print("No se pudo crear el server en la ip: "+ str(ipadress))
    logging.warning("No se pudo crear el server en la ip: "+ str(ipadress))
server_socket.listen(1)

print("Servidor iniciado en "+str(port))
logging.info(str(datetime.datetime.now())+" Servidor iniciado en "+str(port))

try:
    client_socket, client_address = server_socket.accept()
except:
    print("Fallo la recepción del cliente")
    logging.warning("Fallo la recepción del cliente")

print("Conectado a "+str(client_address))
logging.info(str(datetime.datetime.now())+" Conectado a "+str(client_address))


while True:
    try:
        data = client_socket.recv(1024)
    except:
        print("Error de recepción de mensaje")
        logging.warning("Error de recepción de mensaje")
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
    
    try:
        client_socket.sendall(response.encode())
    except:
        print("Fallo en el envío del mensaje")
        logging.warning("Fallo en el envío del mensaje")
        
    logging.info(str(datetime.datetime.now())+" Mensaje enviado codificado: "+ str(response))

client_socket.close()
server_socket.close()
logging.info(str(datetime.datetime.now())+" Servidor cerrado")