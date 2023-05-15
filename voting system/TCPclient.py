import socket            
s = socket.socket()        
port = 7000               
s.connect(('127.0.0.1', port))
vote = input("\nEnter A/B/C : ")
s.send(vote.encode())
print(s.recv(1024).decode())
s.close()    
     