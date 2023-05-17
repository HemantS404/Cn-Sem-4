n = int(input("Enter number of string : "))
dicty={}
for i in range(n):
    j = input(f"Enter {i+1} string : ")
    dicty[i] =[len(j)+1,j]
for i in dicty:
    print(f"{dicty[i][0]}{dicty[i][1]}",end=' ')
