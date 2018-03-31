import socket
s= socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
c = None
while True:
    if c is None:
        print("waiting for connection...")
        c,addr = s.accept()
        print("connected with ",addr)
    else:
        print("waiting for response...")
        print("Client: ",str(c.recv(1024)))
        data = input("Server : ")
        c.send(bytes(data,'UTF-8'))
