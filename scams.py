import requests
import os
import logging
import random
import string
import json

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Scammer Payback 1.0.0] | Configuring URL...")

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

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Scammer Payback 1.0.0] | Configuring Login...")

print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the login Form Data?: ' + Style.RESET_ALL, end="")
usernameInput = input()


# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Scammer Payback 1.0.0] | Configuring Password...")


print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the password Form Data?: ' + Style.RESET_ALL, end="")
passwordInput = input()

# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Scammer Payback 1.0.0] | Configuring Requests...")


#requestInput = int(input(f"{Fore.RED}[SP] {Fore.CYAN}How many requests do you want to make?: {Style.RESET_ALL}"))
#print(requestInput)

print(Fore.RED + "[SP]" + Fore.CYAN + ' How many request do you want to send?: ' + Style.RESET_ALL, end="")
requestInput = int(input())

# ==========================================================================================================

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Scammer Payback 1.0.0] | Configuring Proxy...")


print(Fore.RED + "[SP]" + Fore.CYAN + ' Would you like to use a Proxy?: ' + Style.RESET_ALL, end="")
proxyInput = input()

if "yes" in proxyInput or "no" in proxyInput:
    pass
else:
    print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
    exit()

#if proxyInput == "yes":
    scrapep = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If no, every check will be on random proxy.")
    mult = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Multiple checks for proxy {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
#else:
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If true, before code will be {Fore.WHITE}discord.gift/")
    prefix = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Prefix before codes {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    if "yes" in prefix or "no" in prefix:
        pass
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
        exit()

name_extra = ''.join(random.choice(string.digits))

for i in range(requestInput):
    for i in range(random.randint(19,19)):

        chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
        password = ""
        password = ''.join(random.choice(chars) for i in range(8)) # Or whatever amount of requests you wish to send
        name_extra = ''.join(random.choice(string.digits))
        username = 'Ubhua' + name_extra + '@yahoo.com'

    requests.post(url, allow_redirects=False, data={
		f"{usernameInput}": username,
		f"{passwordInput}": password
	})
    print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

print(f"{Fore.RED}[SP] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")
