#! /usr/bin/python3

import socket

print(
	'''
 ____                                 ____           _     _               
| __ )  __ _ _ __  _ __   ___ _ __   / ___|_ __ __ _| |__ | |__   ___ _ __ 
|  _ \ / _` | '_ \| '_ \ / _ \ '__| | |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
| |_) | (_| | | | | | | |  __/ |    | |_| | | | (_| | |_) | |_) |  __/ |   
|____/ \__,_|_| |_|_| |_|\___|_|     \____|_|  \__,_|_.__/|_.__/ \___|_|   
                                                                           
'''
)

targetIP = input("Target IP > ")
			
def grabit(target, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	
	if port == 80:
		try:
			s.connect((target, port))
			s.send(b"HEAD / HTTP/1.1\r\nUser-Agent: Mozilla/5.0\r\nHost: 127.0.0.1\r\nAccept: */*\r\n\r\n")
			data = s.recv(1024)
			print(data)
			s.close()
		except TimeoutError:
			print("TimeoutError: timed out")
		except ConnectionRefusedError:
			print("ConnectionRefusedError: [Errno 111] Connection refused")
	else:
		try:
			s.connect((target, port))
			s.send(b"HelloThere\r\n")
			data = s.recv(1024)
			print(data)
			s.close()
		except TimeoutError:
			print("TimeoutError: timed out")
		except ConnectionRefusedError:
			print("ConnectionRefusedError: [Errno 111] Connection refused")

while True:
	targetPORT = int(input("Target Port > "))
	grabit(targetIP, targetPORT)
	print()
	newport = input("Check another port? y/n > ")
	print()
	newport = newport.lower()
	if newport == "y":
		continue 
	else:
		print("Exiting...")
		break