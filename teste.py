import csv, socket

target = "www.google.com"

with open('lib/tcp-ports.csv', newline='') as file:
    tcp_ports = csv.reader(file, delimiter=' ', quotechar='|')

def target_validate(target):
        try:
            if target.replace('.', '').isdigit():
                target = socket.gethostbyaddr(target)
            else:
                print(f"Target: {socket.gethostbyname(target)}")
        except socket.herror or socket.gaierror:
            print("[!] Host not found ")

def tcpscan(target):
    whale_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in tcp_ports:
        tcp = (', '.join(i))
        port = "".join(tcp.split(",", 2)[1:2])
        recv = whale_client.connect_ex((target, port))
        if(recv == 0):
            try:
                print(f" {tcp}\n")
            except socket.gaierror:
                pass            
tcpscan(target)