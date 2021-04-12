import requests
import os
import logging
import random
import string
import json
# import grequests

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
# url = urlInput
# print(url)




# print(fore.GREEN + "What is the scammer's URL???: ", end='')
# urlInput = input()
# url = 'https://'+urlInput
# print(url)

# urlInput = "{url}"

# ==========================================================================================================

# usernameInput = input("What is the log in information?: ")
# print(usernameInput)
print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the login Form Data?: ' + Style.RESET_ALL, end="")
usernameInput = input()
# print(usernameInput)


# ==========================================================================================================

# passwordInput = input("What is the password information?: ")
print(Fore.RED + "[SP]" + Fore.CYAN + ' What is the password Form Data?: ' + Style.RESET_ALL, end="")
passwordInput = input()
# print(passwordInput)
# print(passwordInput)

# ==========================================================================================================

requestInput = int(input(f"{Fore.RED}[SP] {Fore.CYAN}How many requests do you want to make?: {Style.RESET_ALL}"))
# print(Fore.RED + "[SP]" + Fore.CYAN + ' How many requests do you want to make?: ' + Style.RESET_ALL, end="".isdecimal())
print(requestInput)

#def notnumber(answer):
#	answer = print(Fore.ORANGE + "[ERROR]" + Fore.CYAN + 'This is not a number')
#	return answer

# requestInput = input(),
#if isdigit() == False:
#    print('Please only enter a number')


# print(requestInput)

# requestInput = input("How many requests do you want to send to the website?: ")
# print(requestInput)
# rangeInput = range(requestInput)

name_extra = ''.join(random.choice(string.digits))

username = 'kingsman' + name_extra + '@yahoo.com'
# password = ''.join(random.choice(chars) for i in range(8))

# requests.post(url, allow_redirects=False, data={
#	'{usernameInput}': username,
# 	'{passwordInput}': password
# })

#for i in range(amt):
#    ending = ""
#    for i in range(random.randint(19,19)):
#        ending += random.choice(chars)
#    url = (main+ending)
#    print(url)

for i in range(requestInput):
    for i in range(random.randint(19,19)):

        chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
        password = ""
        password = ''.join(random.choice(chars) for i in range(8)) # Or whatever amount of requests you wish to send
        name_extra = ''.join(random.choice(string.digits))
        username = 'kingsman' + name_extra + '@yahoo.com'

    requests.post(url, allow_redirects=False, data={
		f"{usernameInput}": username,
		f"{passwordInput}": password
	})
    #for i in range(random.randint(2,2)):
        # print(f"Sending {style.BOLD}{requestInput}{Style.RESET_ALL} requests right now, please wait...")
    print(f"Sending {style.BOLD}1{Style.RESET_ALL} requests with the Username {style.UNDERLINED}{username} and Password {style.UNDERLINED}{password}")

print(f"{Fore.RED}[SP] {Fore.CYAN}Successfully sent {Style.RESET_ALL}{style.BOLD}{requestInput}{Style.RESET_ALL}{Fore.CYAN} requests to {style.UNDERLINED}{url}.")

# p.map(requests.post, urls)

# rs = (grequests.get(u) for u in urls)
# grequests.map(rs)

# Sending ' + Style.BOLD + requestInput + Style.RESET_ALL + ' requests with the Username %s and Password %s' % (username, password

# print(f"Sending {style.BOLD}{requestInput}{Style.RESET_ALL} requests with the Username {username} and Password {password}")

# print('Sending ' + Style.BOLD + requestInput + Style.RESET_ALL + ' requests with the Username %s and Password %s' % (username, password))
