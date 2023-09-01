#! /usr/bin/python3

import socket
import ssl

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
	
	elif port == 443:
		try:
			host = input("Give the server hostname (i.e google.com) > ")
			print()
			Purpose = ssl.Purpose.SERVER_AUTH
			context = ssl.create_default_context(purpose=Purpose)
			with socket.create_connection((target,port)) as sock:
				with context.wrap_socket(sock, server_hostname=host) as ssock:
					ssock.settimeout(2)
					ssock.send("HEAD / HTTP/1.1\r\nUser-Agent: Mozilla/5.0\r\nHost: 1.2.3.4\r\nAccept: */*\r\n\r\n".encode())
					data = ssock.recv(1024).decode()
					print(data)
					ssock.close()
		except ssl.SSLCertVerificationError:
			print("ssl.SSLCertVerificationError: possible hostname mismatch")
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
	newport = input("Check another port for same target? y/n > ")
	print()
	newport = newport.lower()
	if newport == "y":
		continue 
	else:
		print("Exiting...")
		break