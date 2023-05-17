choice = int(input('Enter \n1 : Error detection \n2 : Find transmitted bit stream \n : '))

def xorbit(dividend, divisor):
    x=''
    if (dividend[0] == '1'):
        for i in range (len(dividend)):
            x += str((int(dividend[i])+int(divisor[i]))%2)
    else:
        x=dividend
    return x[1:]

if(choice == 1):
    dataTrans = input("Enter transmitted message: ")
    divisor = input("Enter divisor : ")
    new = dataTrans + '0'*(len(divisor) - 1)
    dividend = new[0:len(divisor)]
    i = len(divisor)
    while i<len(new):
        prod = xorbit(dividend, divisor)
        dividend = prod + new[i]
        i+=1
    remainder = xorbit(dividend, divisor)
    if int(remainder) == 0:
        print("No Error")
    else:
        print("Error")

elif(choice == 2):
    data = input("Enter data to be transmitted : ")
    divisor = input("Enter divisor : ")
    new = data + '0'*(len(divisor) - 1)
    dividend = new[0:len(divisor)]
    i = len(divisor)
    while i < len(new):
        prod = xorbit(dividend, divisor)
        dividend = prod + new[i]
        i+=1
    remainder = xorbit(dividend, divisor)
    print(f"{data}{remainder}")
