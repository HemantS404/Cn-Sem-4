ip = input("\nEnter IP address: ")
ip_array = list(map(eval, ip.split(".")))
if ip_array[0] >= 0 and ip_array[0] <= 127:
    mask = '255.0.0.0'
    ip_class = "Class A"
elif ip_array[0] >= 128 and ip_array[0] <= 191:
    mask = '255.255.0.0'
    ip_class = "Class B"
elif ip_array[0] >= 192 and ip_array[0] <= 223:
    mask = '255.255.255.0'
    ip_class = "Class C"
elif ip_array[0] >= 224 and ip_array[0] <= 239:
    mask = 'multicast'
    ip_class = "Class D"
elif ip_array[0] >= 240 and ip_array[0] <= 255:
    mask = 'reserved'
    ip_class = "Class E"
else:
    mask = 'wrong input'
    print("wrong input ip must be < 256")

if (mask != 'wrong input'):
    subnetAddr_array = []
    if(mask != 'multicast' and  mask != 'reserved'):
        mask_array = list(map(eval, mask.split(".")))
        for i in range(0,4):
            subnetAddr_array.append(str(mask_array[i] & ip_array[i]))
    subnetAddr = '.'.join(subnetAddr_array)
    print("\nThe Subnet Mask for " + ip + " is " + mask)
    print("Subnet Address is " + subnetAddr)
    print("Class of IP Address is " + ip_class + '\n ')