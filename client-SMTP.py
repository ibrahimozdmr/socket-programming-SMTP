import socket

serverName = 'smtp.gmail.com'
serverPort = 587

clientSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print('Sunucudan gelen mesaj: ', clientSocket.recv(1024).decode())

clientSocket.close()