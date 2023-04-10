import logging
import datetime
import socket

port = 10500
logging.basicConfig(filename='client.log', encoding='utf-8', level=logging.DEBUG)
ipadress = input("Ingrese IP a conectar : ")

server_address = (ipadress, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
logging.info(str(datetime.datetime.now())+" Conectado a servidor "+str(server_address))

while True:
    message = input("Ingrese mensaje : ")
    client_socket.sendall(message.encode())
    logging.info(str(datetime.datetime.now())+" Mensaje enviado : "+str(message))
    data = client_socket.recv(1024)
    if not data:
        break
    response = data.decode()
    print("Mensaje recibido : "+str(response))
    logging.info(str(datetime.datetime.now())+" Mensaje recibido : "+str(response))

client_socket.close()
logging.info(str(datetime.datetime.now())+" Conexion finalizada")