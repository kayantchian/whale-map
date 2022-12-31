import socket

class Client():

    def validatehost(self,host):
        try:
            if host.replace('.', '').isdigit():
                host = socket.gethostbyaddr(host)
                print(f"\nName server > {host[0]}\n") 
                #returns a list where 0 position is host name
            else:
                if "www." in host:
                    host = host[4:]
                    pass
                if ".com" not in host:
                    host = host + ".com"
                    pass
                print(f"\nIPv4 > {socket.gethostbyname(host)}\n")
        except:
                print("\n[*] Invalid host\n")
                pass
        return host
