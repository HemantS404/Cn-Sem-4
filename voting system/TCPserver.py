import socket            
s = socket.socket()        
print ("\nTCP Socket successfully created")
port = 7000               
s.bind(('127.0.0.1', port))        
print ("TCP socket binded to %s" %(port))
s.listen(5)    
print ("TCP socket is listening\n")
A = 0
B = 0
C = 0
n = 0           
while (n<3):
    c, addr = s.accept()
    print ('Got connection from', addr )
    k = c.recv(1024).decode()
    if ( k == 'A'):
        A+=1
    elif (k == 'B'):
        B+=1
    elif (k == 'C'):
        C+=1
    else:
        c.send('Wrong Vote'.encode())
    c.send('\nVote counted\nThank you for voting\n '.encode())
    n += 1
    c.close()

print(f'\nA = {A}, B = {B}, C = {C}\n ')