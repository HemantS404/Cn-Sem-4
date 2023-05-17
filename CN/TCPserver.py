import socket

A=B=C=n=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen()

while n<3:
    c, addr = s.accept()
    n+=1
    print(f'Connect with {addr}')
    msg = c.recv(1028)
    c.send(b'Thank You for Voting')
    print(f'Message : {msg.decode()}')
    if(msg.decode() == 'A'):
        A+=1
    elif(msg.decode() == 'B'):
        B+=1
    elif(msg.decode() == 'C'):
        C+=1
    c.close()

print(f'A={A}, B={B}, C={C}')