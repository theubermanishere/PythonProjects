import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)

print >> sys.stderr, 'Starting up on %s port %s' % server_address

sock.bind(server_address)
sock.listen(1)

while True:
    print>> sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    print client_address
