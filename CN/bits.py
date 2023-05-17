data = input("enter the data in bits : ")
count = i = 0
while i < len(data):
    print(data[i],end='')
    if(data[i] == '1'):
        count=1
        i+=1
        while(count<5 and i<len(data)):
            if(data[i] == '1'):
                print(data[i],end='')
                i+=1
                count+=1
            else:
                break
        else:
            if(count == 5):
                print(0,end='')
            count = 0
    else:
        i+=1
