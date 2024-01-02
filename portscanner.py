from datetime import datetime
import sys
import socket

#Definindo o alvo
if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1]) #Endereço IPv4 do alvo a ser escaneado
	port1 = int(sys.argv[2]) #Define o início do range de portas TCP a serem escaneadas
	port2 = int(sys.argv[3]) #Define o fim do range de portas TCP a serem escaneadas
else:
	print('Quantidade de argumentos inválida') #Erro caso a quantidade de argumentos esteja errada, 2 argumentos são necessários para o código funcionar: portscanner.py + IP_DO_ALVO

#Adicionando um banner simples para criar um efeito gráfico
print("-" * 50)
print("Escaneando o endereço: "+target)
print("Início: "+str(datetime.now()))
print("-" * 50)

try: #Processo de escaneio de cada uma das portas TCP do alvo
	for port in range(port1,port2): #Define a faixa de portas TCP que deve ser escaneada
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Utiliza o módulo socket para determinar o IP e as portas TCP
		socket.setdefaulttimeout(1) #Define o tempo máximo que cada porta pode ser escaneada, nesse caso 1 segundo
		result = s.connect_ex((target,port)) #Define os resultados
		if result == 0: 
			print(f'Porta {port} está aberta') #Caso o resultado seja igual a 0, então a porta está aberta
		s.close()

except KeyboardInterrupt: #Interrupção realizada pelo usuário para sair do programa, CTRL + C
	print('\nSaindo do programa')
	sys.exit()

except socket.gaierror: #Erro padrão do módulo socket, caso o endereço IP não seja encontrado
	print('Nome do Host não pôde ser definido')
	sys.exit()
	
except socket.error: #Erro padrão do módulo socket
	print('Não foi possível se conectar ao servidor')
	sys.exit()

