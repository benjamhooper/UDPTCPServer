#import socket module
from socket import *
import sys #In order to terminiate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket (look back at client/server program)
#recall that a webserver listens at port 80
#Fill in start
#fill in end
serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print('Ready to serve..')
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket (the OK message)
		header = 'HTTP/1.1 200 OK\r\n\r\n'
		connectionSocket.send(outputdata(header.encode())		
		#send the content of the requested file to the client
		for i in range(0, len(outputdata)):
		connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()
	except IOError:
		print('error')
		#send response
		#fill in start 
		#fill in end
		#close client socket
		#fill in start
		#fill in end

serverSocket.close()
sys.exit() #terminate the program after sending coresponding data

