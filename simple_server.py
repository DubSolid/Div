import http.server
import socketserver
import socket
import os
import sys

def server():

    directory = os.getcwd()
    ip_addr = socket.gethostbyname(socket.gethostname())

    port = input('Enter port to serve server on: ')
    try:
        port = int(port)
    except ValueError:
        print(f"Invalid input, {port} is not a valid integer.")
        return

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print(f'Serving on: {directory} with IP & port {ip_addr}:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.exit()

server()