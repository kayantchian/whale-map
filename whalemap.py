from portscan import *
import sys, argparse

class WhaleMap(object):

    def __init__(self):
        parser=argparse.ArgumentParser(
        prog = 'WhaleMap',
        epilog='by kayantchian',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
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
                                    '.    '-'Y \._  /   
                                        '--;____'--.'-,1
                                         /..'       '''        
                                       Help
                        --------------------------------
           This script performs a TCP port scanning through the socket library
           There is a default csv file that contains all tcp ports and services, 
           but you can provide one as well via the command (-f), as long as it's up 
           to the same standards.
        """)
        parser.add_argument('-p', '--portscan', metavar='url',help='specify url site')
        parser.add_argument('-f', '--file', metavar='file',default='lib/tcp-ports.csv', help="specify a csv file of ports")
        self.args=vars(parser.parse_args())
        try:
            parser.print_help()
        except argparse.ArgumentError:
            print('\nCatching an argumentError')
        

    def main(self):
        if(self.args["portscan"]):
            portscan = Scan(self.args['portscan'],self.args['file'])
            portscan.tcpscan()
whale = WhaleMap()
whale.main()