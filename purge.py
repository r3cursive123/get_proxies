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
    ____                      
   / __ \__  ___________ ____ 
  / /_/ / / / / ___/ __ `/ _ \\
 / ____/ /_/ / /  / /_/ /  __/
/_/    \__,_/_/   \__, /\___/ 
                 /____/       

    ''' + "\n","yellow")

banner()

print colored("Removing current proxychains.conf" + "\n","red")
os.system("rm proxychains.conf")
print colored("Copying our custom proxychains config file" + "\n","red")
shutil.copy("proxychains.conf.template","proxychains.conf")
print colored("Done!" + "\n" ,"blue")
print colored("You may now run proxy_scrape.py to get a fresh list" + "\n" ,"yellow")
