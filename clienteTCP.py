#!/usr/bin/python

import socket
host = "192.168.0.12"
porta = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, porta))
s.send("GET /HTTP/1.1\r\nFoooda-se\r\n\r\n")
response = s.recv(5000)
print response
