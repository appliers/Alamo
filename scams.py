import requests
import os
import logging
import random
import string
import json

from colored import fore, back, style

from colorama import Fore, Back, Style

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

from colorama import init
init()
from colorama import Fore, Back, Style

print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the scam URL?: ' + Style.RESET_ALL, end="")
urlInput = input()
url = 'https://'+urlInput

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

request = requests.get(url, headers=headers)
if request.status_code == 400:
    print('This website does not exist bruh')

# ==========================================================================================================

print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the login Form Data?: ' + Style.RESET_ALL, end="")
usernameInput = input()


# ==========================================================================================================

print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the password Form Data?: ' + Style.RESET_ALL, end="")
passwordInput = input()

# ==========================================================================================================

requestInput = int(input(f"{Fore.RED}[SP] {Fore.CYAN}How many requests do you want to make?: {Style.RESET_ALL}"))
print(requestInput)

name_extra = ''.join(random.choice(string.digits))

username = 'kingsman' + name_extra + '@yahoo.com'

for i in range(requestInput):
    for i in range(random.randint(19,19)):

        chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
        password = ""
        password = ''.join(random.choice(chars) for i in range(8)) # Or whatever amount of requests you wish to send
        name_extra = ''.join(random.choice(string.digits))
        names = json.loads(open('names.json').read())
        username = 'kingsman' + name_extra + '@yahoo.com'

    requests.post(url, allow_redirects=False, data={
		f"{usernameInput}": username,
		f"{passwordInput}": password
	})
    print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

print(f"{Fore.RED}[SP] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")
