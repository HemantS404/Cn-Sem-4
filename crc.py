choice = int(input('\n\033[34mEnter (1/2) \n1.Data to Transmitted \n2.Error Detection \n\033[0m : '))

if not (choice == 1 or choice == 2):
    print("\n\033[31mWrong input\033[0m\n ")
else:
    old_data = input("\n\033[34mEnter data\033[0m : ")
    divisor = input("\033[34mEnter divisor\033[0m : ")

    len_divisor = len(divisor)
    data = old_data + '0'*(len_divisor-1)
    len_data = len(data)

    def xorbit(divisor,dividend):
        x=''
        if(dividend[0] == '1'):
            for i in range(len(divisor)):
                x += str((int(divisor[i]) + int(dividend[i]))%2)
        else:
            x = dividend
        return x[1:]


    dividend = data[0:len_divisor]
    i = len_divisor
    while(i < len_data):
        prod = xorbit(divisor=divisor, dividend=dividend)
        dividend = prod + data[i]
        i+=1
    else:
        remainder = xorbit(divisor=divisor, dividend=dividend)

    if choice == 1:
        print('\n\033[34mThe Data Transmitted\033[0m : '+f'\033[34m{old_data}\033[0m'+f'\033[32m\x1B[4m{remainder}\x1B[0m\033[0m'+'\n ')
    elif choice == 2:
        remainder = int(remainder)
        if remainder:
            print(f"\n\033[31m\x1B[4mError\x1B[0m\033[0m \033[34mas the remainder is\033[0m \033[31m\x1B[4m{remainder}\x1B[0m\033[0m\n ")
        else:
            print(f"\n\033[32m\x1B[4mNo Error\x1B[0m\033[0m \033[34mas the remainder is\033[0m \033[32m\x1B[4m{remainder}\x1B[0m\033[0m\n ")