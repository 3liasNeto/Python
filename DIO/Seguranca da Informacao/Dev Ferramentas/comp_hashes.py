import hashlib

arq1 = 'DIO/Seguranca da Informacao/Dev Ferramentas/hashes.txt'
arq2 = 'DIO/Seguranca da Informacao/Dev Ferramentas/hashes2.txt'

hsh = hashlib.sha256()
hsh.update(open(arq1,'rb').read())

hsh2 = hashlib.sha256()
hsh2.update(open(arq2,'rb').read())

if hsh.digest() != hsh2.digest() :
    print(f'O arquivo: {arq1} e diferente do arquivo : {arq2}')
    print('O hash do arquivo arq1 e: ', hsh.hexdigest())
    print('O hash do arquivo arq2 e: ', hsh2.hexdigest())
else:
    print(f'O arquivo : {arq1} e igual a o arquivo: {arq2}')