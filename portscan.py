import socket, csv

class Scan(object):

    def __init__(self, host):
        self.target = host
        with open('lib/tcp-ports.csv', newline='') as file:
            tcp_ports = csv.reader(file, delimiter=' ', quotechar='|')
            try:
                if self.target.replace('.', '').isdigit():
                    self.target = socket.gethostbyaddr(self.target)
                    print(f"Host: {self.target[0]}")
                else:
                    print(f"Host: {socket.gethostbyname(self.target)}")
            except socket.herror or socket.gaierror:
                pass
    

    def tcpscan(self):
        whale_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for i in tcp_ports:
            tcp = (', '.join(i))
            port = "".join(tcp.split(",", 2)[1:2])
            recv = whale_client.connect_ex((self.target, port))
            if(recv == 0):
                try:
                    print(f" {tcp}\n")
                except socket.gaierror:
                    pass

nmap = Scan('142.251.135.132')
