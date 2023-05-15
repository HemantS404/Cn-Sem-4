data_stream = input("\n\033[34mEnter the data stream\033[0m : ")
n = len(data_stream)
if(n!=11):
    data_stream = '0'*(11-n) + data_stream
new_data = data_stream[0:7]+'0'+data_stream[7:10]+'0'+data_stream[10]+'0'+'0'

sumy=0
for i in range(0,8):
    sumy += int(new_data[i])
p8 = sumy%2

sumy=0
for i in range(0,4):
    sumy += int(new_data[i])
for i in range(8,11):
    sumy += int(new_data[i])
p4 = sumy%2

sumy=0
for i in range(0,2):
    sumy += int(new_data[i])
for i in range(4,6):
    sumy += int(new_data[i])
for i in range(8,10):
    sumy += int(new_data[i])
for i in range(12,13):
    sumy += int(new_data[i])
p2 = sumy%2

sumy=0
for i in range(0,15,2):
    sumy += int(new_data[i])
p1 = sumy%2
# print(p8,p4,p2,p1)
listy = []
listy2 = []
for i in range(14,-1,-1):
    if (i == 7 or i == 3 or i == 1 or i == 0):
        listy.append('P'+str(i+1))
    else:
        listy.append('D'+str(i+1))
for i in new_data:
    listy2.append(i)
for i in range(0,15):
    if (i == 7):
        listy2[7] = str(p8) 
    elif (i ==3):
        listy2[11] = str(p4)
    elif (i == 1):
        listy2[13] = str(p2)
    elif(i == 0):
        listy2[14] = str(p1)
print()
for i in listy:
    print(f"\033[31m{i}\033[0m" , end ='\t')
print()
for i in listy2:
    print(f"\033[32m{i}\033[0m", end ='\t')
print("\n ")