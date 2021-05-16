#!/usr/bin/python3

import socket

HOST = '127.0.0.1' # localhost
PORT = 6969

# Create socket object that supports the context manager `with`, so there's no need for s.close)_
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # initialize
    s.listen() # listen for connections
    conn, addr = s.accept() # accept any connection

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

