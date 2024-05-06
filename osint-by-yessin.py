# This tool is made by Yessin (https://github.com/Yessingit)
# Do not copy this code without permission

import os
import sys
import platform
from colorama import init, Fore
from googlesearch import search
import requests
from bs4 import BeautifulSoup

init()

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a', jsname='UWckNb'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

def google_search(query):
    query = '"' + query + '"'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    params = {"q": query, "num": 1000, "hl": "nl", "gl": "nl"}
    response = requests.get("https://www.google.com/search", headers=headers, params=params)
    links = extract_links(response.text)

    script_dir = os.path.dirname(os.path.realpath(__file__))

    folder_path = os.path.join(script_dir, "searches")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"{query}.txt"
    file_path = os.path.join(folder_path, filename)

    with open(file_path, "w") as f:
        for link in links:
            f.write(f"Link found: {link}\n")

    print(Fore.GREEN + "OSINT search:", query)
    print(Fore.WHITE + "")
    print(Fore.GREEN + "Link Found:")
    for link in links:
        print(Fore.RED + link)
    print(Fore.WHITE + "")
    print(Fore.GREEN + f"{len(links)} links are saved (/searches/{filename})")

    input(Fore.GREEN + "Press Enter to continue...")
    clear_terminal()
    main()

def main():
    print(Fore.YELLOW + '''
     ____      _       _                       _       
    / __ \    (_)     | |                     (_)      
   | |  | |___ _ _ __ | |_ _   _  ___  ___ ___ _ _ __  
   | |  | / __| | '_ \| __| | | |/ _ \/ __/ __| | '_ \ 
   | |__| \__ \ | | | | |_| |_| |  __/\__ \__ \ | | | |
    \____/|___/_|_| |_|\__|\__, |\___||___/___/_|_| |_|
                            __/ |                         Made by Yessin (https://github.com/Yessingit)
                           |___/                          Version: 1.0
''')
    query = input(Fore.GREEN + "OSINT search: ")
    try:
        google_search(query)
    except KeyboardInterrupt:
        print(Fore.RED + "Exiting...")
        sys.exit()

if __name__ == "__main__":
    clear_terminal()
    main()
