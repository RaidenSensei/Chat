import socket
import sys
import time

s = socket.socket()
host = input(str("Please Enter The Hostname Of The Server:"))
port = 8080
s.connect((host,port))
print("Connected to the chat server")
while 1:
    incomming_message = s.recv(1024)
    incomming_message = incomming_message.decode()
    print("Server:" , incomming_message)
    print("")

    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("Message has been sent:")
    print("")
