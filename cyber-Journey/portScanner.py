import socket

target = "127.0.0.1"

for port in [80, 443, 22, 21]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"port {port} is open")
        else:
            print(f"port {port} is closed")
    finally:
         sock.close()
        