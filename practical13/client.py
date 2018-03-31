import socket
s= socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))
print("connected to ",host)
while True:
    data = input("Client : ")
    s.send(bytes(data,'UTF-8'))
    print("waiting for response")
    print("Server : ",str(s.recv(1024)))
