import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'Client Hi!',('127.0.0.1', 8000))
msg, addr = s.recvfrom(1028)
print(f'Msg : {msg.decode()}')