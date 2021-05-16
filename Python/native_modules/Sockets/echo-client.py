#!/usr/bin/python3

import socket

HOST = "127.0.0.1" # Server's hostname or IP address
PORT = 6969

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hello, from the other side...")
    data = s.recv(1024)

print("Received", repr(data))
