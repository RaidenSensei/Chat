import socket
import sys
import time

###end of imports###

### init ###

s = socket.socket()
host = socket.gethostname()
print("server will start on host: "+host)
port = 8080
s.bind((host,port))
print("")
print("Server done binding to host and port successfully:")
print("")
print("Serer is waiting for incoming connection:")
s.listen(1)
conn, addr = s.accept()
print(addr,"Has connected to the server and is now online...")
print("")
while True:
    message=input(str(">>"))
    message=message.encode()
    conn.send(message)
    print("Message has been sent:")
    print("")

    incomming_message = conn.recv(1024)
    incomming_message = incomming_message.decode()
    print("Server:", incomming_message)
    print("")

