import socket

def banner():
	print('-' * 50)

banner()
HOST = socket.gethostbyname(input('Hostname: '))
print('The hostname IPv4 Address is: '+HOST)
banner()
