from portscan import *
import sys

class WhaleMap(object):

    def main(self):
        print("""
            ██╗    ██╗██╗  ██╗ █████╗ ██╗     ███████╗    ███╗   ███╗ █████╗ ██████╗ 
            ██║    ██║██║  ██║██╔══██╗██║     ██╔════╝    ████╗ ████║██╔══██╗██╔══██╗
            ██║ █╗ ██║███████║███████║██║     █████╗      ██╔████╔██║███████║██████╔╝
            ██║███╗██║██╔══██║██╔══██║██║     ██╔══╝      ██║╚██╔╝██║██╔══██║██╔═══╝ 
            ╚███╔███╔╝██║  ██║██║  ██║███████╗███████╗    ██║ ╚═╝ ██║██║  ██║██║     
            ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
                                                __       __
                                                    '.'--.--'.-'
                                    .,_------.___,   /' r'
                                    ', '-._a      '-' .'
                                    '.    '-'Y \._  /   by kayantchian
                                        '--;____'--.'-,1
                                    hi  /..'       '''        
        """)
        while True:
            try:
                op = int(input('[1] Port Scan\n[2] DNS Enum\n[3] Exit\n>> '))
                if(op==3):
                    sys.exit(0)
                if(op==1):
                    host = input("Host: ")
                    portscan = Scan(host)
                    portscan.tcpscan()
            except ValueError:
                pass

whale = WhaleMap()
whale.main()