import os 
import time

with open('DIO/Seguranca da Informacao/ping/host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(ip)
        os.system('ping -c 2 ' + ip)
        time.sleep(5)