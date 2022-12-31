import nmap
from whale_client import Client

class Scan(Client):
    def __init__(self, host):
        try:
            self.target = super().validatehost(self.target)
        except:
            print('\n[*] Error on args')

    def nmap(self):
        nm = nmap.PortScanner()
        nm = scan(self.target)        
a = Scan("www.google.com")

