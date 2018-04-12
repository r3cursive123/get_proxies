import shutil
from termcolor import colored
import os

os.system("clear")

# Check if we are running as root
if os.geteuid() != 0:
    print('You must run this script as root!!!')
    exit()

def banner():
    print colored('''
   _____      __            
  / ___/___  / /___  ______ 
  \__ \/ _ \/ __/ / / / __ \\
 ___/ /  __/ /_/ /_/ / /_/ /
/____/\___/\__/\__,_/ .___/ 
                   /_/      
''' + "\n","yellow")


banner()

print colored("Creating backup of original proxychains.conf" + "\n","red")
shutil.copy("/etc/proxychains.conf","/etc/proxychains.conf.orig")
print colored("Backup created as /etc/proxychains.conf.orig" + "\n","blue")
print colored("Copying our custom proxychains config file to /etc" + "\n","red")
os.system("rm /etc/proxychains.conf")
shutil.copy("proxychains.conf","/etc/proxychains.conf")
print colored("Copied!" + "\n" ,"blue")
print colored("You may now run proxy_scrape.py" + "\n" ,"yellow")


