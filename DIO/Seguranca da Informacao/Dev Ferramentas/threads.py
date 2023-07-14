from threading import Thread
import time

def jato(v, p):
    trj = 0
    v =  v**3 if v < 5 else v*1
    while trj <= 200:
        print(f'Jato V | Piloto: {p} | KM: {trj}\n')
        trj += v
        time.sleep(1)

jato_1 = Thread(target=jato, args=[2,'Daniel'])
jato_2 = Thread(target=jato, args=[1,'Pedro'])    

jato_1.start()
jato_2.start()  