import requests
import os
from colorama import Fore, Style, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

header = [
    Fore.WHITE + " ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗",
    Fore.RED + " ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝",
    Fore.WHITE + " ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ ",
    Fore.RED + " ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ ",
    Fore.WHITE + " ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗",
    Fore.RED + "  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝",
    Fore.WHITE + "                                                             "
    
]

for line in header:
    print(line)

webhook_url = input(Fore.RED + "Enter the Discord webhook URL: " + Style.RESET_ALL)
message = input(Fore.WHITE + "Enter the message to send: " + Style.RESET_ALL)
count = int(input(Fore.RED + "Enter the number of times to send the message: " + Style.RESET_ALL))

for i in range(count):
    try:
        data = {
            "content": message
        }
        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print(Fore.RED + f"Message sent successfully ({i + 1}/{count})!" + Style.RESET_ALL)
        else:
            print(Fore.WHITE + f"Failed to send message ({i + 1}/{count}): {response.status_code} - {response.text}" + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"ERROR {e}" + Style.RESET_ALL)

input(Fore.BLUE + "enter to exit" + Style.RESET_ALL)