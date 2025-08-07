import socket
import threading
import time

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"port {port} is open.")
        sock.close()
    except:
        pass

print( "Port Scanner v2 mit threading")
target = input("Enter target IP: ")
start_time = time.time()

threads = []
for port in range(1, 1001):
    thread=threading.Thread(target=scan_port, args=(target, port))
    thread.start()
    threads.append(thread)

for thread in threads:
       thread.join()

print(f"Scan completed in {time.time() - start_time:,.2f} seconds")