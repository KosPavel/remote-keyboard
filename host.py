import socket
import time

from press_simulation import PressKey, ReleaseKey
from keybinds import Keybinds

HOST = socket.gethostbyname(socket.gethostname())
PORT = 50005

print('my IP = ' + HOST + ', ready to connection')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
print('Connected by', addr)

while True:
    try:
        data = ''
        data = conn.recv(1024).decode('UTF-8')
        if data[0] == '!':
            data = data[2:(len(data)-1)]
            ReleaseKey(Keybinds[data])
        else:
            data = data[1:(len(data)-1)]
            PressKey(Keybinds[data])
    except:
        print('Mate, slow down please!')
