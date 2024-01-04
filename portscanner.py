#!/bin/python3

from datetime import datetime
import sys
import socket

def visual_lines():
    print('-' * 50)

def banner(target):
    visual_lines()
    print(f"Escaneando o endereço: {target}")
    print(f"Início: {str(datetime.now())}")
    visual_lines()

def scan(target, port1, port2):
    try:
        for port in range(port1, port2 + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)

            result = s.connect_ex((target, port))

            if result == 0:
                print(f'A porta {port} está aberta')
            s.close()
    except KeyboardInterrupt:
        print('\nSaindo do programa')
        sys.exit()
    except socket.gaierror:
        print('Nome do Host não pôde ser definido')
        sys.exit()
    except socket.error:
        print('Não foi possível se conectar ao servidor')
        sys.exit()

def main():
    visual_lines()
    print('|0|: Unico endereço')
    print('|1|: Lista de endereços')
    mode = int(input('Selecione o modo: '))

    if mode == 0:
        visual_lines()
        target = socket.gethostbyname(input('Digite o endereço do alvo: '))
        port1 = int(input('Digite a primeira porta TCP: '))
        port2 = int(input('Digite a ultima porta TCP: '))
        banner(target)
        scan(target, port1, port2)

    elif mode == 1:
        filename = input('Digite o nome do arquivo: ')
        with open(filename) as archive:
            ip_list = archive.read().splitlines()
        port1 = int(input('Digite a primeira porta TCP: '))
        port2 = int(input('Digite a ultima porta TCP: '))
        for ip in ip_list:
            target = ip
            banner(target)
            scan(target, port1, port2)

    else:
        print('Selecione um modo válido')

if __name__ == "__main__":
    main()
