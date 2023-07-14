import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Conexao Falhou: "+ e)
        sys.exit()
    print("Socket Criado com Sucesso")

    host_alvo = input("ip: ")
    porta = int(input("porta do ip: "))
    
    try:
        s.connect((host_alvo, porta))
        print(f'Cliente TCP Conctado com sucesso na Host: {host_alvo}, na porta:{porta}')
        s.shutdown(2)
    except socket.error as e:
        print("Conexao Falhou: "+ e)
        sys.exit()
        
if __name__ == "__main__" :
    main()

        