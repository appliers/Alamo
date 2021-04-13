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

print(f"\n")
print(f"{Fore.RED}[Anoma] {Fore.GREEN}Select a number from 1 - 6 to continue{Style.RESET_ALL}")
print(f"[{Fore.GREEN}1{Style.RESET_ALL}] {Fore.CYAN}Start{Style.RESET_ALL}")
print(f"[{Fore.GREEN}2{Style.RESET_ALL}] {Fore.CYAN}Help{Style.RESET_ALL}")
print(f"[{Fore.GREEN}3{Style.RESET_ALL}] {Fore.CYAN}Settings{Style.RESET_ALL}")
print(f"[{Fore.GREEN}4{Style.RESET_ALL}] {Fore.CYAN}View{Style.RESET_ALL}")
print(f"[{Fore.GREEN}5{Style.RESET_ALL}] {Fore.CYAN}About{Style.RESET_ALL}")
print(f"[{Fore.GREEN}6{Style.RESET_ALL}] {Fore.CYAN}Exit{Style.RESET_ALL}")
optionInput = input("> ")

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Anoma 1.0.0] | Configuring URL...")

print(Fore.RED + "[Anoma]" + Fore.CYAN + ' What is the scam URL?: ' + Style.RESET_ALL, end="")
urlInput = input()
url = 'https://'+urlInput

#request = requests.get(f"{url}")
#if request.status_code == 200:
#    pass
#else:
#    print(f'{url} is not a valid URL. Please try a different URL.')


# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Anoma 1.0.0] | Configuring Login...")

print(Fore.RED + "[Anoma]" + Fore.CYAN + ' What is the login Form Data?: ' + Style.RESET_ALL, end="")
usernameInput = input()


# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Anoma 1.0.0] | Configuring Password...")


print(Fore.RED + "[Anoma]" + Fore.CYAN + ' What is the password Form Data?: ' + Style.RESET_ALL, end="")
passwordInput = input()

# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Anoma 1.0.0] | Configuring Requests...")


#requestInput = int(input(f"{Fore.RED}[SP] {Fore.CYAN}How many requests do you want to make?: {Style.RESET_ALL}"))
#print(requestInput)

print(Fore.RED + "[Anoma]" + Fore.CYAN + ' How many request do you want to send?: ' + Style.RESET_ALL, end="")
requestInput = int(input())

# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Anoma 1.0.0] | Configuring Proxy...")


print(Fore.RED + "[Anoma]" + Fore.CYAN + ' Would you like to use a Proxy?: ' + Style.RESET_ALL, end="")
proxyInput = input()

if "yes" in proxyInput or "no" in proxyInput:
    pass
else:
    print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
    exit()

if proxyInput == "yes":

    httpInput = input(f"What is the HTTP proxy?: ")
    httpsInput = input(f"What is the HTTPS proxy?: ")

    http_proxy  = f"http://{httpInput}"
    https_proxy = f"https://{httpsInput}"


    proxyDict = {
        "http"  : http_proxy,
        "https" : https_proxy,
        }

    name_extra = ''.join(random.choice(string.digits))

    for i in range(requestInput):
        for i in range(random.randint(19,19)):

            chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
            password = ""
            password = ''.join(random.choice(chars) for i in range(8)) # Or whatever amount of requests you wish to send
            name_extra = ''.join(random.choice(string.digits))
            username = 'kingsman' + name_extra + '@yahoo.com'

        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        requests.post(url, allow_redirects=False, headers={'User-Agent': 'Chrome'}, proxies=proxyDict, data={
        	f"{usernameInput}": username,
        	f"{passwordInput}": password
    	})
        print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

    print(f"{Fore.RED}[Anoma] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")

else:
    name_extra = ''.join(random.choice(string.digits))

    for i in range(requestInput):
        for i in range(random.randint(19,19)):

            chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
            password = ""
            password = ''.join(random.choice(chars) for i in range(8)) # Or whatever amount of requests you wish to send
            name_extra = ''.join(random.choice(string.digits))
            username = 'kingsman' + name_extra + '@yahoo.com'

        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        requests.post(url, allow_redirects=False, headers={'User-Agent': 'Chrome'}, data={
    		f"{usernameInput}": username,
    		f"{passwordInput}": password
    	})
        print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

    print(f"{Fore.RED}[Anoma] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")
