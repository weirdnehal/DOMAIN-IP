# Domain to ip Convert

from termcolor import colored
print(colored("************Domain to ip convert************",'green'))

print(colored("************Create By Weird Nehal************",'red'))

import socket
import pyfiglet #banner 

banner = colored(pyfiglet.figlet_format("Domain to Ip Convert"), 'green')
print(banner)
domain_name = input("Please, Enter your Target Domain Name:")

ip = socket.gethostbyname(domain_name)

print("Ip for {} : {}".format(domain_name,ip))
