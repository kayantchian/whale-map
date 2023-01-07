import nmap 

class Nmap():
    def __init__(self, host):
        self.target = host

    def scan(self):
        nm = nmap.PortScanner()
        nm.scan(self.target, "22-443")

a = Nmap("www.google.com")
a.scan()
