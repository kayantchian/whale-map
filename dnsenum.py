import socket, dns.resolver
from whale_client import Client

class Dns(Client):
    def __init__(self, host, file):
        self.file = file
        self.target = super().validatehost(host)
        with open("brute-force.txt") as wordlist: #open the file that contains subdomains wordlist
            dns = wordlist.readlines()

    def brutednsnum(self):
        for name in dns:
            DNS = name.strip("\n") + "." + self.host
            try:
                print(DNS + ": " + socket.gethostbyname(DNS))
            except socket.gaierror:
                pass

    def registerenum(self):
        registers = ["A", "AAAA", "MX", "NS"]
        for re in registers:
            recv = dns.resolver.query(self, re, raise_on_no_answer=False) #3
            if recv.rrset is not None:
                print(recv.rrset)


