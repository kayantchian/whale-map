import socket 
import dns.resolver as dns
from whale_client import Client

class Dns(Client):
    def __init__(self, host, ):
        #self.file = file
        self.target = super().validatehost(host)
        #with open("brute-force.txt") as wordlist: #open the file that contains subdomains wordlist
            #dns = wordlist.readlines()

    def brutednsnum(self):
        for name in dns:
            DNS = name.strip("\n") + "." + self.host
            try:
                print(DNS + ": " + socket.gethostbyname(DNS))
            except socket.gaierror:
                pass

    def registerenum(self):
        registers = ["A", "AAAA", "MX", "NS", "CNAME"]
        for re in registers:
            recv = dns.resolve(self, re) #3
            if recv.rrset is not None:
                print(recv.rrset)
a = Dns("www.google.com")
a.registerenum