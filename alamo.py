import requests
import os
import logging
import random
import string
import json
import sys
import time
from requests.exceptions import ConnectionError

# Added the [Error] tag to errors such as in line 40;

from colored import fore, back, style

from colorama import Fore, Back, Style

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

from colorama import init
init()
from colorama import Fore, Back, Style

#import ctypes
#ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Menu")
print(f"\n")

print(f'{Style.BRIGHT}{Fore.BLUE}  ▄▄▄       ██▓    ▄▄▄      ███▄ ▄███▓ ▒█████         ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ▒████▄    ▓██▒   ▒████▄   ▓██▒▀█▀ ██▒▒██▒  ██▒      ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ▒██  ▀█▄  ▒██░   ▒██  ▀█▄ ▓██    ▓██░▒██░  ██▒      ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██▒██    ▒██ ▒██   ██░      ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ▓█   ▓██▒░██████▒▓█   ▓██▒██▒   ░██▒░ ████▓▒░       ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░▒░▒░        ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ░   ▒▒ ░░ ░ ▒  ░ ░   ▒▒ ░  ░      ░  ░ ▒ ▒░         ')
print(f'{Style.BRIGHT}{Fore.BLUE}  ░   ▒     ░ ░    ░   ▒  ░      ░   ░ ░ ░ ▒          ')
print(f'{Style.BRIGHT}{Fore.BLUE}      ░  ░    ░        ░         ░       ░ ░          ', Style.RESET_ALL)


print(f"\n")
print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.GREEN}Select a number from 1 - 6 to continue{Style.RESET_ALL}")
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
    print(f"[{Fore.BLACK}{Style.BRIGHT}Error{Style.RESET_ALL}] [{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}Answer must be between 1 - 6")
    exit()

if optionInput == "1":
#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring URL...")

    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What is the scam URL?: {Style.RESET_ALL}", end="")
    urlInput = input()
    url = 'https://'+urlInput

    if url == "":
        print(f"You didn't enter a URL idiot")
    else:
        pass

    try:
        response = requests.get(url, allow_redirects=True, headers={'User-Agent': 'Chrome'})
    except ConnectionError:
        print(f"[{Fore.RED}Error{Style.RESET_ALL}] {Fore.GREEN}{url} is not a valid website. Please try again.")
        exit()
    except ValueError:
        print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}You haven't inputted anything. Please try again.{Style.RESET_ALL}")
        exit()
    else:
        pass

    #request = requests.get(f"{url}")
    #if request.status_code == 200:
    #    pass
    #else:
    #    print(f'{url} is not a valid URL. Please try a different URL.')


    # ==========================================================================================================

#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Login...")

    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What is the login Form Data?: {Style.RESET_ALL}", end="")
    usernameInput = input()

    #try:
    #    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What is the login Form Data?: {Style.RESET_ALL}", end="")
    #    usernameInput = input()
    #except ValueError:
    #    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}You didn't enter anything! Please try again.{Style.RESET_ALL}")
    #    exit()



    # ==========================================================================================================

#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Password...")


    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What is the password Form Data?: {Style.RESET_ALL}", end="")
    passwordInput = input()

    #try:
    #    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What is the password Form Data?: {Style.RESET_ALL}", end="")
    #    passwordInput = input()
    #except ValueError:
    #    print(f"[]{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}You didn't enter anything! Please try again.{Style.RESET_ALL}")
    #    exit()

    # ==========================================================================================================

#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Requests...")


    #requestInput = int(input(f"{Fore.RED}[SP] {Fore.CYAN}How many requests do you want to make?: {Style.RESET_ALL}"))
    #print(requestInput)

    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}How many requests do you want to send?: {Style.RESET_ALL}", end="")

    request2Input = input()

    if not request2Input.isdecimal():
        raise Exception(f'\n{style.BOLD}[{Fore.RED}Error{Style.RESET_ALL}] {Fore.GREEN}"{request2Input}" is not a number. Please a valid number')
    else:
        pass

    requestInput = int(request2Input)

    # =============================================================================================================

    #requestInput = int(input())

    #request2Input = requestInput

    # requestInput = int(request2Input)

    # ==========================================================================================================

#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Configuring Proxy...")


    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What you like to use a Proxy?: {Style.RESET_ALL}", end="")
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

        import ctypes
    #    ctypes.windll.kernel32.SetConsoleTitleW(f"[Alamo 1.0.1] | Sending {requestInput} requests to {url}")
    #
        name_extra = ''.join(random.choice(string.digits))

        for i in range(requestInput):
            for i in range(random.randint(19,19)):

                chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
                password = ""
                password = ''.join(random.choice(chars) for i in range(8)) # Or whatever amount of requests you wish to send
                name_extra = ''.join(random.choice(string.digits))
                username = 'Kingsman' + name_extra + '@gmail.com'

                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

            # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

            requests.post(url, allow_redirects=False, headers=header, proxies=proxyDict, data={
            	f"{usernameInput}": username,
            	f"{passwordInput}": password
        	})
# raise ProxyError(f'\n{style.BOLD}[{Fore.RED}Error{Style.RESET_ALL}] {Fore.GREEN}"{request2Input}" Failed to connect to the proxies. Please try again.')

            print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

        print(f"{Fore.RED}[Alamo] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")

    #    import ctypes
    #    ctypes.windll.kernel32.SetConsoleTitleW(f"[Alamo 1.0.1] | Successfully sent {requestInput} to {url}")

    else:
    #    import ctypes
    #    ctypes.windll.kernel32.SetConsoleTitleW(f"[Alamo 1.0.1] | Sending {requestInput} requests to {url}")

        name_extra = ''.join(random.choice(string.digits))

        for i in range(requestInput):
            for i in range(random.randint(19,19)):

                chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
                password = ""
                password = ''.join(random.choice(chars) for i in range(12)) # Or whatever amount of requests you wish to send
                name_extra = ''.join(random.choice(string.digits))
                username = 'Kingsman' + name_extra + '@gmail.com'

            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

            requests.post(url, allow_redirects=False, headers=header, data={
            	f"{usernameInput}": username,
                f"{passwordInput}": password
        	})

            print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

        print(f"{Fore.RED}[Alamo] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")

#        import ctypes
    #    ctypes.windll.kernel32.SetConsoleTitleW(f"[Alamo 1.0.1] | Successfully sent {requestInput} to {url}")

if optionInput == "2":
#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Help")

    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.GREEN}What do you need help with? Choose an option below:{Style.RESET_ALL}")
    print(f"[{Fore.MAGENTA}1{Style.RESET_ALL}] {Fore.CYAN}Starting Alamo{Style.RESET_ALL}")
    print(f"[{Fore.MAGENTA}2{Style.RESET_ALL}] {Fore.CYAN}Settings{Style.RESET_ALL}")
    print(f"[{Fore.MAGENTA}3{Style.RESET_ALL}] {Fore.CYAN}Check{Style.RESET_ALL}")
    print(f"[{Fore.MAGENTA}4{Style.RESET_ALL}] {Fore.CYAN}Other{Style.RESET_ALL}")

    helpInput = input("> ")
    if "1" in helpInput or "2" in helpInput or "3" in helpInput or "4" in helpInput:
        pass
    else:
        print(f"[{Fore.MAGENTA}Alamo{Style.RESET_ALL}] {Fore.CYAN}Answer must be between 1 - 4")
        exit()

    if helpInput == "1":
        print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.GREEN}Look through this list to see your problem and copy and paste the link into a browser", Style.RESET_ALL)
        print("\n")
        print(f"[{Fore.MAGENTA}Form Data{Style.RESET_ALL}]: {Fore.CYAN}https://github.com/xkwm1/Alamo/blob/main/help/Start/Form-Data.md{Style.RESET_ALL}")
        print(f"[{Fore.MAGENTA}Proxy{Style.RESET_ALL}]: {Fore.CYAN}https://github.com/xkwm1/Alamo/blob/main/help/Start/Proxy.md{Style.RESET_ALL}")

    if helpInput == "2":
        print(f"[{Fore.MAGENTA}Settings{Style.RESET_ALL}]: {Fore.CYAN}'Settings' is coming soon...", Style.RESET_ALL)

    if helpInput == "3":
        print(f"[{Fore.MAGENTA}Check{Style.RESET_ALL}]: {Fore.CYAN}'Check is' coming soon...", Style.RESET_ALL)

    if helpInput == "4":
        print(f"[{Fore.MAGENTA}Other{Style.RESET_ALL}]: {Fore.CYAN}'Others' is coming soon...", Style.RESET_ALL)
        print(f"[{Fore.MAGENTA}What is Alamo?{Style.RESET_ALL}]: {Fore.CYAN}'What is Alamo?' is coming soon...", Style.RESET_ALL)


if optionInput == "3":
#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo ] | Settings")

    print(f"Coming Soon...")

if optionInput == "4":
#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | Check")

    print(f'[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}What website would you like to check? (Do not include "https://" in the URL.):', Style.RESET_ALL, end="")
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

    print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}Would you like to see the code of {url}?{Style.RESET_ALL}")
    codeInput = input("> ")

    if "yes" in codeInput or "no" in codeInput:
        pass
    else:
        print(f"[{Fore.RED}Alamo{Style.RESET_ALL}] {Fore.CYAN}Answer must be either {Style.RESET_ALL}{style.BOLD}yes{Style.RESET_ALL} {Fore.CYAN}or {Style.RESET_ALL}{style.BOLD}no{Style.RESET_ALL}")
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

#    import ctypes
#    ctypes.windll.kernel32.SetConsoleTitleW("[Alamo 1.0.1] | About")
if optionInput == "6":
    exit();
