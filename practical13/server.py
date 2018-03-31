import socket
from _thread import *
s= socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(10)
c = None
def con(c,addr):
    while True:
        try:
            print("connected with ",addr)
            print("Client: ",str(c.recv(1024)))
            data = input("Server : ")
            c.send(bytes(data,'UTF-8'))
        except:
            pass
while True:
    c,addr = s.accept()
    start_new_thread(con,(c,addr))
