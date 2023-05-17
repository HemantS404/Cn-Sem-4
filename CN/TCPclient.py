import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1',8000))
vote = input("Vote (A/B/C) : ")
s.send(vote.encode())
msg = s.recv(1028)
print(f'Message : {msg.decode()}')
s.close()