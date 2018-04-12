import shutil
from termcolor import colored
import os

# Check if we are running as root
if os.geteuid() != 0:
    print('You must run this script as root!!!')
    exit()
os.system("clear")
print colored("Removing current proxychains.conf" + "\n","red")
os.system("rm /etc/proxychains.conf")
print colored("Copying our custom proxychains config file to /etc" + "\n","red")
shutil.copy("proxychains.conf","/etc/proxychains.conf")
print colored("Copied!" + "\n" ,"red")
print colored("You may now run proxy_scrape.py to get a fresh list" + "\n" ,"yellow")
