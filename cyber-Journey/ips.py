import os 
import time
time.sleep(2)

ips  = ["8.8.8.8", "192.168.0.1", "127.0.0.1"]
for ip in ips:
    response = os.system("ping -c 1 " + ip)
    print(ip, "is online!" if response == 0 else "is offline!")
 