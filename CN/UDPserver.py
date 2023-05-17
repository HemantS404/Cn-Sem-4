import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1',8000))

while True:
    msg, addr = s.recvfrom(1028)
    print(f'Connected to : {addr}')
    print(f'Msg : {msg.decode()}')
    s.sendto(b'Server Hi!', addr)
    if msg:
        break