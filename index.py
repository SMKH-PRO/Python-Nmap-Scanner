import nmap


scanner = nmap.PortScanner()


print("Hi, This is a basic nmap automation tool")
ip_address= input("Please enter the ip address: ")
print("The IP address you entered is: ", str(ip_address))

resp = input("""\n
Please enter the type of scan you want to run:

1). SYN ACK SCAN
2). UDP SCAN
3). Comprehensive Scan



""")

print("You've selected option: ", str(resp))

if resp == "1":
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("open ports: ",scanner[ip_address]['tcp'].keys())
