from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('192.168.2.101', 1201))
# while
while True:
    sock.send(b'\xe4\x01\x00\x00\x00\xff\x00\x00')
    data = sock.recv(20)
    print(data)

kk = b'\xe4\x01\x04\x00\x00\xfb\x01\x10\x80@\xff'
