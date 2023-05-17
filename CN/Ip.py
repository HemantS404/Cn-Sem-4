ip_address = list(map(int, input("Enter IP addres : ").split('.')))

def getSubnetAdd(subnet_adr):
    subnet_adr = list(map(str, subnet_adr))
    subnet = subnet_adr[0]+'.'+subnet_adr[1]+'.'+subnet_adr[2]+'.'+subnet_adr[3]
    return subnet

if(ip_address[0] <= 127):
    ip_class = 'A'
    mask = "255.255.255.0"
    subnet_adr = ip_address
    subnet_adr[3] = 0
    subnet = getSubnetAdd(subnet_adr)
elif(ip_address[0] <= 191):
    ip_class = 'B'
    mask = "255.255.0.0"
    subnet_adr = ip_address
    subnet_adr[3] = 0
    subnet_adr[2] = 0
    subnet = getSubnetAdd(subnet_adr)
elif(ip_address[0] <= 223):
    ip_class = 'C'
    mask = "255.0.0.0"
    subnet_adr = ip_address
    subnet_adr[3] = 0
    subnet_adr[2] = 0
    subnet_adr[1] = 0
    subnet = getSubnetAdd(subnet_adr)
elif(ip_address[0] <= 239):
    ip_class = 'D'
    mask = None
    subnet = None
elif(ip_address[0] <= 255):
    ip_class = 'E'
    mask = None
    subnet = None
print(f"IP Belongs to class {ip_class}")
print(f"Subnet mask {mask}")
print(f"Subnet Address : {subnet}")

