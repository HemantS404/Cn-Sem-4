import socket            
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)        
print ("\nUDP Socket successfully created")
port = 7000               
s.bind(('127.0.0.1', port))        
print ("UDP socket binded to %s" %(port))
print ("UDP socket is listening\n")
A = 0
B = 0
C = 0
n = 0           
while (n<3):
    data, addr = s.recvfrom(1024)
    k = data.decode()
    print ('Got connection from', addr )
    if ( k == 'A'):
        A+=1
    elif (k == 'B'):
        B+=1
    elif (k == 'C'):
        C+=1
    else:
        s.sendto('Wrong Vote'.encode(), addr)
    s.sendto('\nVote counted\nThank you for voting\n '.encode(), addr)
    n += 1

s.close()
print(f'\nA = {A}, B = {B}, C = {C}\n ')