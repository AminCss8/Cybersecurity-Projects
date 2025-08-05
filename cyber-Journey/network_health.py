import socket
import os;os.system('afplay /system/library/sounds/Ping.aiff')

print("""\033[94m
  █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀▀ █▀█ █▀▀ █▀ █▀   █▀▀ █▄ █ ▀█▀
  █▄▄ █▀█ █ ▀ █ ██▄   █▄▄ █▄█ ██▄ ▄█ ▄█   ██▄ █ ▀█  █ 
\033[0m""")

def main():
    target = input("Ziel-IP oder Domain: ")
    
    # Ping-Check
    print("\n[1/3] 🔍 Ping-Check...")
    response = os.system(f"ping -c 1 {target} > /dev/null 2>&1")
    if response == 0:
        print("   ✅ Host erreichbar!")
    else:
        print("   ❌ Host nicht erreichbar!")
    
    # Port-Check (nur wenn erreichbar)
    if response == 0:
        print("\n[2/3] 🔒 Port-Scan...")
        for port in [21, 22, 80, 443, 3306, 8080]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.7)
            try:
                sock.connect((target, port))
                print(f"   ✅ Port {port} offen")
            except:
                print(f"   ❌ Port {port} geschlossen", end='\r')
            finally:
                sock.close()
    
    # DNS-Check
    print("\n\n[3/3] 🌐 DNS-Auflösung...")
    try:
        ip = socket.gethostbyname(target)
        print(f"   🔗 {target} = {ip}")
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            print(f" Reverse-DNS: {hostname}")
        except:
            print("   ❌ DNS-Fehler!")
    except:
        print(" DNS-Fehler!")

if __name__ == "__main__":
    main()
     