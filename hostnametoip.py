import socket

def banner():
	print('-' * 50)

banner()
HOST = socket.gethostbyname(input('Digite o endereço do alvo: '))
print('O endereço IPv4 do alvo é: '+HOST)
banner()
