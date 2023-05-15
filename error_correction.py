data = list(input("\n\033[34mEnter The code\033[0m : "))
for i in range (0,7):
    if(i == 3):
        p4 = int(data[i])
    elif(i == 5):
        p2 = int(data[i])
    elif(i == 6):
        p1 = int(data[i])

sum4 = 0
for i in range(0,3):
    sum4 += int(data[i])
sum4 = sum4%2

if(sum4 == p4):
    p4 =  0
else:
    p4 = 1

sum2 = 0
for i in range(0,2):
    sum2 += int(data[i])
for i in range(4,5):
    sum2 += int(data[i])
sum2 = sum2%2

if(sum2 == p2):
    p2 =  0
else:
    p2 = 1

sum1 = 0
for i in range(0,1):
    sum1 += int(data[i])
for i in range(2,3):
    sum1 += int(data[i])
for i in range(4,5):
    sum1 += int(data[i])
sum1 = sum1%2

if(sum1 == p1):
    p1 =  0
else:
    p1 = 1
pos =  p4*4 + p2*2 + p1
og_data = ''
corrected_data = ''
for i in range (len(data)):
    if i == (7-pos):
        corrected_data += str(int(not int(data[i])))
    else:
        corrected_data += data[i]
    og_data += data[i]
if pos>0:
    print("\nError at", f"\033[31m{pos}th\033[0m", "position bit","\n\033[34mOriginal Code\033[0m\t:  ", f"\033[31m{og_data}\033[0m","\n\033[34mCorrected Code\033[0m\t:  ", f"\033[32m{corrected_data}\033[0m\n ")
else:
    print("\n\033[32mNo error\033[0m", "\n\033[34mOriginal Code\033[0m\t:  ", f"\033[32m{og_data}\033[0m\n ")