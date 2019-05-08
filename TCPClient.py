from socket import *

serverName = '192.168.4.170'
serverPort = 12001
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('input message to server: ')

clientSocket.sendto(message.encode(),(serverName,serverPort))
messageFromServer,serverAddress = clientSocket.recvfrom(2048)
print(messageFromServer.decode())
clientSocket.close()
