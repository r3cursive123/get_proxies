# get_proxies

This program is used to scrape a  website that has a list of free socks4 and socks5 proxies - it then writes IP/Port info into /etc/proxychains.conf for use.

My recommendation is to use the proxychains.conf example configuration included with this repo as it provides the best chance of anonymity by using random_chain and a minimum of 4 chained proxies. Of course, this can all be changed by editing proxychains.conf to your liking.

# Dependencies: 
shred (used for secure deletion of temp files), proxychains, python 2.6*

# Usage:
1. git clone https://github.com/r3cursive123/get_proxies.git
2. cd get_proxies
3. "sudo python setup.py" - this will create a backup of /etc/proxychains.conf and copy our config file template to replace /etc/proxychains.conf

Only run setup.py once!!!

4. "sudo python proxy_scrape.py"

If you want to get a fresh list of proxies, please run "sudo purge.py" which will remove the current /etc/proxychains.py and copy our custom template back to /etc/proxychains.conf

