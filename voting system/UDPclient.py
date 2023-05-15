import socket            
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)        
port = 7000
vote = input("\nEnter A/B/C : ")
s.sendto(vote.encode(), ('127.0.0.1', port))
print(s.recvfrom(1024)[0].decode())
s.close()    
     