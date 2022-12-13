import socket, csv

class Scan(object):

    def __init__(self, host, file = 'lib/tcp-ports.csv'):
        self.target = host
        self.file = file
        with open(self.file, newline='') as list:
            dict = csv.DictReader(list, fieldnames= ["Type", "Port", "Service"])
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
        for port in self.ports:
            recv = whale_client.connect_ex((self.target, port))
            if(recv == 0):
                try:
                    print(f" {tcp}\n")
                except socket.gaierror:
                    pass

nmap = Scan('google.com')
#nmap.tcpscan()