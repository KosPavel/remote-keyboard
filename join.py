import socket

from pynput.keyboard import Key, Listener

def on_press(key):
    data = str(key)
    print('key pressed: ' + data)
    conn.send(bytes(data, 'UTF-8'))

def on_release(key):
    data = str(key)
    print('key released: ' + data)
    data = '!' + data
    conn.send(bytes(data, 'UTF-8'))

''' establishing connection '''
conn = socket.socket()

HOST = input("Enter IP of remote PC")
PORT = 50005
conn.connect((HOST, PORT))

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
