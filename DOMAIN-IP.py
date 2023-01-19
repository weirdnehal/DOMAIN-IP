# Domain to ip Convert
logo =                                          """   
\033[1;99m╔═══════════════════════════════════════════════════╗
\033[1;92m█   ##    ## ######## ##     ##    ###    ##        █
\033[1;93m█   ###   ## ##       ##     ##   ## ##   ##        █
\033[1;94m█   ####  ## ##       ##     ##  ##   ##  ##        █
\033[1;95m█   ## ## ## ######   ######### ##     ## ##        █
\033[1;96m█   ##  #### ##       ##     ## ######### ##        █
\033[1;97m█   ##   ### ##       ##     ## ##     ## ##        █
\033[1;98m█   ##    ## ######## ##     ## ##     ## ########  █
\033[1;99m╚═══════════════════════════════════════════════════╝

\033[1;91m╔═══════════════════════════════════════════════════╗
\033[1;92m█             DEVELOPER : NEHAL AHMED               █
\033[1;93m█             GITHUB    : weirdnehal                █
\033[1;96m█             WHATSAPP  : +8801613016943            █
\033[1;91m╚═══════════════════════════════════════════════════╝
           
    """            

import socket
import pyfiglet #banner 

banner = colored(pyfiglet.figlet_format("Domain to Ip Convert"), 'green')
print(banner)
domain_name = input("Please, Enter your Target Domain Name:")

ip = socket.gethostbyname(domain_name)

print("Ip for {} : {}".format(domain_name,ip))
