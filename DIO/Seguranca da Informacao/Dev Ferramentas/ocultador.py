import ctypes

oc = 0x02

ret = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', oc)

if ret:
    print("Arquivo foi ocultado")
else:
    print("Arquivo nao foi ocultado")