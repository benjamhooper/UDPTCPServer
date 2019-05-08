from socket import *

serverPort = 12000
severSocket = socket(AF_INET,SOCK_DGRAM)
severSocket.bind(('localhost',serverPort))

while True:
	message,clientAddress = severSocket.recvfrom(2048)
	print message();
	severSocket.sendto('hello', clientAddress)
	if message == 'close':
		print 'closeAlready'
		severSocket.close()
		break

