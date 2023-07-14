import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado')

host = 'localhost'
port = 5454

s.bind((host,port))
msg = 'SERVER: HI'

while True:
    dados, end = s.recvfrom(4096)

    if dados:
        print("SERVER: SENDING MESSAGE")
        s.sendto(dados + (msg.encode()), end)