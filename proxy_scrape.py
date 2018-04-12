from bs4 import BeautifulSoup
import requests
import re
import os
import csv
from collections import defaultdict
from termcolor import colored


# Check if we are running as root
if os.geteuid() != 0:
    print('You must run this script as root!!!')
    exit()

# Number of IP's to add..
max = raw_input("How many proxies shall we add? ")

target = "/etc/proxychains.conf"
page = requests.get("https://www.socks-proxy.net/")
soup = BeautifulSoup(page.content, 'html.parser')

# Snag html tags == <tr>
p = soup.find_all("tr")

# Open temp file and write results
with open("ips.csv", "w") as f:
    for element in p:
        new = re.sub('<[^<]+?>', ',', str(element)).replace(",,",",")
        f.writelines(new + "\n")

# Parse temp file and add to config file
columns = defaultdict(list)
with open('ips.csv',"r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (b, c) in row.items():
            columns[b].append(c)
    ip = columns['IP Address']
    port = columns['Port']
    ver = columns['Version']
    i = 0
    while i < int(max):
        test = str(ver[i]).lower()
        if test == "socks4" or test == "socks5":
            final = (str(ver[i]).lower() + " " + str(ip[i]) + " " + str(port[i]))
            os.system("echo " + final + " >> " + target)
            print colored("Proxy " + final + " added!","red")
            i+=1
        else:
            i+=1

# Trash the temp file
destroy='shred -uz '
os.system(destroy + "ips.csv")
