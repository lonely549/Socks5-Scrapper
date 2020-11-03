import webbrowser
import time
import urllib
import urllib.request

intro = """
╔═══╗        ╔╗          ╔═══╗    ╔═══╗                           
║╔═╗║        ║║          ║╔══╝    ║╔═╗║                           
║╚══╗╔══╗╔══╗║║╔╗╔══╗    ║╚══╗    ║╚══╗╔══╗╔═╗╔══╗ ╔══╗╔══╗╔══╗╔═╗
╚══╗║║╔╗║║╔═╝║╚╝╝║══╣    ╚══╗║    ╚══╗║║╔═╝║╔╝╚ ╗║ ║╔╗║║╔╗║║╔╗║║╔╝
║╚═╝║║╚╝║║╚═╗║╔╗╗╠══║    ╔══╝║    ║╚═╝║║╚═╗║║ ║╚╝╚╗║╚╝║║╚╝║║║═╣║║ 
╚═══╝╚══╝╚══╝╚╝╚╝╚══╝    ╚═══╝    ╚═══╝╚══╝╚╝ ╚═══╝║╔═╝║╔═╝╚══╝╚╝ 
                                                   ║║  ║║         
                                                   ╚╝  ╚╝         

Socks 5 scrapper By Lonely549"""


print(intro)
time.sleep(3)


content=urllib.request.urlopen("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all")
for line in content:
    print (line)

time.sleep(2)

print("latest socks 5 Scrapped")
time.sleep(50)

