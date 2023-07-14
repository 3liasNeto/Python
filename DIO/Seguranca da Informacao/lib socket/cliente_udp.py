import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket Criado com Sucesso!!')
host = "localhost"
porta = 5433
msg = "Hello World"

try:
    print(f'Cliente: {msg}')
    s.sendto(msg.encode(), (host, 5454))
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechado a Conexao')
    s.close()