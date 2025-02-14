import requests
import time
from colorama import Fore
import os
import ctypes

y = "\033[93m"
w = "\033[0m"
b = "\033[94m"

def webhookspamtitle():
    print(f"{y}Webhook Spam Tool by rumanoooo{w}")

def webhookspam():
    os.system('cls')
    webhookspamtitle()
    print(f"""{y}[{w}+{y}]{w} Webhook url for spam: """)
    webhook = input(f"""{y}[{b}#{y}]{w} WebHook: """)
    print(f"""\n\n{y}[{b}+{y}]{w} Message to spam: """)
    message = input(f"""{y}[{b}#{y}]{w} Message: """)
    print(f"""\n\n{y}[{w}+{y}]{w} Amount of time for the attack: """)
    timer = input(f"""{y}[{b}#{y}]{w} Amount: """)
    input(f"""\n\n\n\n{y}[{b}#{y}]{w} Press ENTER to Valid""")

    try:
        timeout = time.time() + 1 * float(timer) + 0.5

        while time.time() < timeout:
            response = requests.post(
                webhook,
                json = {"content" : message},
                params = {'wait' : True}
            )
            os.system('cls')
            time.sleep(1)
            if response.status_code == 204 or response.status_code == 200:
                print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Message sent""")
            elif response.status_code == 429:
                print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Rate limited ({response.json()['retry_after']}ms)""")
                time.sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error code: {response.status_code}""")
    except:
        print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Your request is invalid !""")
        time.sleep(2)
        os.system('cls')
        main()
    
webhookspam()
