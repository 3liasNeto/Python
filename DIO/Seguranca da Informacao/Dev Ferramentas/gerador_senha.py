import random, string

tam = int(input("Qual deve ser o tamanho da Senha: "))
qtds = int(input("Quantas senhas voce deseja: "))
res = input("Gerar senha? Sim ou Nao: ")
res = res.lower()
char = string.ascii_letters + string.digits + '@#$%&*()?/><;:'
rnd = random.SystemRandom()

for _ in range(qtds):
    if res == "sim":
        print(''.join(rnd.choice(char) for i in range(tam)))
