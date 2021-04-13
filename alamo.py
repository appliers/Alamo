import requests
import os
import logging
import random
import string
import json
import sys
from requests.exceptions import ConnectionError
import colorful as cf

from colored import fore, back, style

from colorama import Fore, Back, Style

ci_colors = {
    'mint': '#c5e8c8',  # RGB hex value
    'darkRed': '#c11b55',  # RGB hex value
    'lightBlue': (15, 138, 191),  # RGB channel triplet
    'pink': '#FFC0CB'
}

cf.use_palette(ci_colors)

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

from colorama import init
init()
from colorama import Fore, Back, Style

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Menu")

print(f"\n")
print(f"{Fore.RED}[Alamo] {Fore.GREEN}Select a number from 1 - 6 to continue{Style.RESET_ALL}")
print(f"[{Fore.GREEN}1{Style.RESET_ALL}] {Fore.CYAN}Start{Style.RESET_ALL}")
print(f"[{Fore.GREEN}2{Style.RESET_ALL}] {Fore.CYAN}Help{Style.RESET_ALL}")
print(f"[{Fore.GREEN}3{Style.RESET_ALL}] {Fore.CYAN}Settings{Style.RESET_ALL}")
print(f"[{Fore.GREEN}4{Style.RESET_ALL}] {Fore.CYAN}Check{Style.RESET_ALL}")
print(f"[{Fore.GREEN}5{Style.RESET_ALL}] {Fore.CYAN}About{Style.RESET_ALL}")
print(f"[{Fore.GREEN}6{Style.RESET_ALL}] {Fore.CYAN}Exit{Style.RESET_ALL}")
optionInput = input("> ")

if "1" in optionInput or "2" in optionInput or "3" in optionInput or "4" in optionInput or "5" in optionInput or "6" in optionInput:
    pass
else:
    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}Answer must be between 1 - 6")
    exit()

if optionInput == "1":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring URL...")

    print(Fore.RED + "[Alamo]" + Fore.CYAN + ' What is the scam URL?: ' + Style.RESET_ALL, end="")
    urlInput = input()
    url = 'https://'+urlInput

    try:
        response = requests.get(url, allow_redirects=True, headers={'User-Agent': 'Chrome'})
    except ConnectionError:
        print(f"{style.BOLD}[{Fore.RED}Error{Style.RESET_ALL}] {Fore.GREEN}{url} is not a valid website. Please try again.")
        exit()
    else:
        pass

    #request = requests.get(f"{url}")
    #if request.status_code == 200:
    #    pass
    #else:
    #    print(f'{url} is not a valid URL. Please try a different URL.')


    # ==========================================================================================================

    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Login...")

    print(Fore.RED + "[Alamo]" + Fore.CYAN + ' What is the login Form Data?: ' + Style.RESET_ALL, end="")
    usernameInput = input()


    # ==========================================================================================================

    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Password...")


    print(Fore.RED + "[Alamo]" + Fore.CYAN + ' What is the password Form Data?: ' + Style.RESET_ALL, end="")
    passwordInput = input()

    # ==========================================================================================================

    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Requests...")


    #requestInput = int(input(f"{Fore.RED}[SP] {Fore.CYAN}How many requests do you want to make?: {Style.RESET_ALL}"))
    #print(requestInput)

    print(Fore.RED + "[Alamo]" + Fore.CYAN + ' How many request do you want to send?: ' + Style.RESET_ALL, end="")

    request2Input = input()

    if not request2Input.isdecimal():
        raise Exception(f'\n{style.BOLD}[{Fore.RED}Error{Style.RESET_ALL}] {Fore.GREEN}"{request2Input}" is not a number. Please a valid number')
    else:
        pass

    requestInput = int(request2Input)

    #requestInput = int(input())

    #request2Input = requestInput

    # requestInput = int(request2Input)

    # ==========================================================================================================

    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Proxy...")


    print(Fore.RED + "[Alamo]" + Fore.CYAN + ' Would you like to use a Proxy? (Choose "no" unless you want to be spammed with errors): ' + Style.RESET_ALL, end="")
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

        print(f"{Fore.RED}[Alamo] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")

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

        print(f"{Fore.RED}[Alamo] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")


if optionInput == "2":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Help")

    print(f"{Fore.RED}[Alamo] {Fore.GREEN}What do you need help with? Choose an option below:{Style.RESET_ALL}")
    print(f"[{Fore.GREEN}1{Style.RESET_ALL}] {Fore.CYAN}Starting Alamo{Style.RESET_ALL}")
    print(f"[{Fore.GREEN}2{Style.RESET_ALL}] {Fore.CYAN}Settings{Style.RESET_ALL}")
    print(f"[{Fore.GREEN}3{Style.RESET_ALL}] {Fore.CYAN}Check{Style.RESET_ALL}")
    print(f"[{Fore.GREEN}4{Style.RESET_ALL}] {Fore.CYAN}Other{Style.RESET_ALL}")

    helpInput = input("> ")
    if "1" in helpInput or "2" in helpInput or "3" in helpInput or "4" in helpInput:
        pass
    else:
        print(f"[{Fore.MAGENTA}Hydra{Style.RESET_ALL}] {Fore.CYAN}Answer must be between 1 - 4")
        exit()

    if helpInput == "1":
        print(f"coming soon")

    if helpInput == "2":
        print(f"coming soon")

    if helpInput == "3":
        print(f"coming soon")

    if helpInput == "4":
        print(f"coming soon")


if optionInput == "3":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo ] | Settings")

    print(f"Coming Soon...")

if optionInput == "4":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Check")

    print(f'{Fore.RED}[Alamo] {Fore.CYAN}What website would you like to check? (Do not include "https://" in the URL.):', Style.RESET_ALL, end="")
    checkInput = input()

    url = 'https://'+checkInput

    #response = requests.get(url, allow_redirects=True, headers={'User-Agent': 'Chrome'})
    #print(response.headers)
    try:
        response = requests.get(url, allow_redirects=True, headers={'User-Agent': 'Chrome'})
    except ConnectionError:
        print(f"{style.BOLD}[{Fore.RED}Error{Style.RESET_ALL}] {Fore.GREEN}{url} is not a valid website. Please try again.")
        exit()
    else:
        response = requests.get(url, allow_redirects=True, headers={'User-Agent': 'Chrome'})
        print(response.headers)

    print(f"{Fore.RED}[Alamo] {Fore.CYAN}Would you like to see the code of {url}?{Style.RESET_ALL}")
    codeInput = input("> ")

    if "yes" in codeInput or "no" in codeInput:
        pass
    else:
        print(f"{Fore.RED}[Alamo] {Fore.CYAN}Answer must be either {Style.RESET_ALL}{style.BOLD}yes{Style.RESET_ALL} {Fore.CYAN}or {Style.RESET_ALL}{style.BOLD}no{Style.RESET_ALL}")
        # exit()

    if codeInput == 'yes':
        print("\n")
        print(response.text)
    if codeInput == 'no':
        exit()

if optionInput == "5":
    print(f"[{Fore.GREEN}Name{Style.RESET_ALL}]: Alamo")
    print(f"[{Fore.GREEN}Version{Style.RESET_ALL}]: 1.0.1")
    print(f"[{Fore.GREEN}Developer{Style.RESET_ALL}]: xKwm1")
    print(f"[{Fore.GREEN}Licence{Style.RESET_ALL}]: Apache License 2.0 (Read here: https://github.com/xkwm1/Alamo/blob/main/LICENSE)")
    print(f"[{Fore.RED}Website{Style.RESET_ALL}]: Coming Soon{Style.RESET_ALL}")
    print(f"[{Fore.RED}Discord{Style.RESET_ALL}]: Coming Soon{Style.RESET_ALL}")
    print(f"[{Fore.RED}GitHub{Style.RESET_ALL}]: https://github.com/xkwm1/Alamo{Style.RESET_ALL}")

    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | About")
if optionInput == "6":
    exit();
