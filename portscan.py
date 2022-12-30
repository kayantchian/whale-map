import csv, socket
from whale_client import Client

class Scan(Client):
    def __init__(self, host, file):
        try:
            self.path_file = file
            self.target = super().validatehost(self.target)
            with open(self.path_file, newline='') as list:
                self.dict = [*csv.DictReader(list, fieldnames= ["Type", "Port", "Service"])]
            
        except:
            print('\n[*] Error on args')

    def tcpscan(self):
        whale_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("TYPE   PORT     SERVICE")
        for row in self.dict:
            port = int(row['Port'])
            recv = whale_client.connect_ex((self.target, port))
            if(recv == 0):
                try:
                    tcp_results = next(item for item in self.dict if item["Port"] == str(port))
                    print(f"{tcp_results.get('Type')}    {tcp_results.get('Port')}    {tcp_results.get('Service')}")
                except socket.gaierror:
                    pass

a = Scan("www.google.com", "lib/tcp-ports.csv")

