import socket, csv

class Scan(object):

    def __init__(self, host, file):
        self.target = host
        self.path_file = file
        with open(self.path_file, newline='') as list:
            self.dict = [*csv.DictReader(list, fieldnames= ["Type", "Port", "Service"])]
            try:
                if self.target.replace('.', '').isdigit():
                    self.target = socket.gethostbyaddr(self.target)
                    print(f"IP > {self.target[0]}") 
                    #returns a list where 0 position is host name
                else:
                    print(f"Name server > {socket.gethostbyname(self.target)}")
            except socket.herror or socket.gaierror:
                pass
    
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


