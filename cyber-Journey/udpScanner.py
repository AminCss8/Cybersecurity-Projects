import socket

def udpScanner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.sendto(b"", (ip, port))
        sock.recvfrom(1024)
        print(f"UDP port {port} is open")
    except socket.timeout:
        print(f"UDP is open but no response from {ip}:{port}")
    except Exception as e:
        print(f"UDP port {port} is closed or error occured {e}")
    finally:
        sock.close()

udpScanner("192.168.0.1", 53)

