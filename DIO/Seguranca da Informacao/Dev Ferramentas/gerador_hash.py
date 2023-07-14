import hashlib


string = input("Digite um texto pra gerar uma hash: ")
menu = int(input('''Escolha o Tipo de HASH
        1 - MD5
        2 - SHA1
        3 - SHA256
        4 - SHA512 
        
        '''))

if menu == 1:
    res = hashlib.md5(string.encode('utf-8'))
    print("O Hash da string e: ", res.hexdigest())
elif menu == 2:
    res = hashlib.sha1(string.encode('utf-8'))
    print("O Hash da string e: ", res.hexdigest())
elif menu == 3:
    res = hashlib.sha256(string.encode('utf-8'))
    print("O Hash da string e: ", res.hexdigest())
elif menu == 4:
    res = hashlib.sha512(string.encode('utf-8'))
    print("O Hash da string e: ", res.hexdigest())
else:
    print("Erro")
