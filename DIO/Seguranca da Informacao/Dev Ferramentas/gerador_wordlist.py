import itertools
string = input("Digite um texto: ")
res = itertools.permutations(string,len(string))

for i in res:
    print(''.join(i))