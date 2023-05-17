data = input("Enter Data : ")
start = input("Enter Starting delimiter : ")
end = input("Enter Ending delimiter : ")
print(start,end='')
for i in data:
    if i == start:
        print(start,end='')
    elif i == end :
        print(end,end='')
    print(i,end='')
print(end)