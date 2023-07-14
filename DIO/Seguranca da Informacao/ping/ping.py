import os

ip_ou_host = input("Digite um IP: ")
n = int(input("numero de sequences: "))

os.system(f'ping -c {n} {ip_ou_host}')