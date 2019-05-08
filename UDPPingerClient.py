# UDPPingerClient.py

from socket import *
import time

IP = "127.0.0.1"	# IP address to ping
PORT = 12000	# Port to ping on

lost_packets = 0
response_times = []

# Create a UDP socket for the client
csocket = socket(AF_INET, SOCK_DGRAM)
csocket.settimeout(1)

# Loop through the packet sending procedure 10 times
for i in range(10):
	
	# Set up all the parameters
	sequence = i + 1
	current_time = time.time() * 1000
	message = ("Ping " + str(sequence) + " " + str(current_time))
	
	# Send the packet
	csocket.sendto(message.encode(),(IP,PORT))

	# Listen for a response
	try:
		response, address = csocket.recvfrom(1024)
		sending_time = response.split()[2]
		rtt = (time.time() * 1000) - float(sending_time)
		print("Reply from " + IP + ": " + "Ping " + str(sequence) + " " + time.asctime() + "\nRTT: " + str(rtt))
		response_times.append(rtt)
		
	except timeout:
		print("Request timed out")
		lost_packets += 1

