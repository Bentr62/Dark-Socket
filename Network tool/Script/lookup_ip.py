import re
import requests
import sys
import os
import socket
from datetime import *
from threading import *
from concurrent.futures import ThreadPoolExecutor
from colorama import *
import subprocess
import nmap

init(autoreset=True)

if sys.platform.startswith("win"):
    os.system("cls")
else:
    os.system("clear")

def main_banner():
 print(f"""{Fore.CYAN}
        ╭──────────────────────────────────────────────╮
        │               IP SCANNER TOOL                │
        ╰──────────────────────────────────────────────╯
                {Style.RESET_ALL}""")

main_banner()



def is_valid_ip(ip):
    modele = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(modele, ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False



while True:
    ip = input(f"{Fore.CYAN}Press 'q' or 'quit' to quit or 'r' to return main\nIp : {Style.RESET_ALL}").strip()

    if ip in ['q', 'quit']:
        quit()
    elif ip == 'r':
        subprocess.run([sys.executable, "./main.py"])
        quit() 
    elif is_valid_ip(ip):
        break
    else:
        print(f"{Fore.RED}Commande invalide. Tape 'q', 'quit' ou 'r'.{Style.RESET_ALL}")

if sys.platform.startswith("win"):
    os.system("cls")
else:
    os.system("clear")

main_banner()



try:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    info = response.json()

    valid = "Success" if info.get('status') == 'success' else "invalide"
    country = info.get('country')
    countryCode = info.get('countryCode')
    region = info.get('region')
    regionName = info.get('regionName')
    city = info.get('city')
    zip = info.get('zip')
    lat = info.get('lat')
    lon = info.get('lon')
    timezone = info.get('timezone')
    isp = info.get('isp')
    org = info.get('org') 
    aS = info.get('as')
    query = info.get('query')
except Exception as e:
    print("Erreur :", e)

if org == "":
    org = "Pas d'organisation" 

print(f"""{Fore.YELLOW}
        ╭───────────────[ INFORMATION IP ]───────────────╮
                                  {Style.RESET_ALL}
                Status = {valid}
                Pays = {country}
                Code Alpha du pays = {countryCode}
                Region = {region}
                Nom de region = {regionName}
                Vile = {city}
                Code postal = {zip}                                                                
                latitude = {lat}
                longitude = {lon}
                Fuseau horaire = {timezone}
                Fournisseur d'accès Internet : {isp}
                Organisation = {org}
                Systeme autonome = {aS}
                Lien maps : https://www.google.com/maps?q={lat},{lon}
                Adresse ip : {query}
{Fore.YELLOW}
        ╭───────────────[ SCAN DES PORTS ]──────────────╮
            L'analyse peut prendre du temps selon la 
            configuration de votre machine.{Style.RESET_ALL}""")

open_ports = []
lock = Lock() 

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            with lock:  
                open_ports.append(port)
        sock.close()
    except Exception as e:
        print(f"Erreur pendant le scan du port {port}: {e}")

def scan_ports(ip):
    with ThreadPoolExecutor(max_workers=65535) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(1, 65535)]
        for future in futures:
            future.result() 

scan_ports(ip)

if open_ports:
    print(f"""{Fore.LIGHTGREEN_EX}
        ╔══════════════════════════════════════════════╗
        ║     RÉSULTATS DU SCAN DES PORTS OUVERTS      ║
        ╚══════════════════════════════════════════════╝{Style.RESET_ALL}
""")
    
    for port in open_ports:
        print(f"                {Fore.GREEN}Port {port} {Fore.RESET}(ouvert)")
else:
    print(f"\n{Fore.LIGHTRED_EX}Aucun port ouvert trouvé{Style.RESET_ALL}")


print("""
        
      
        ╔════════════════════════════════════════════════════╗
        ║     Détection de services actif sur les ports      ║
        ╚════════════════════════════════════════════════════╝
      

      
      
      
      
      """)






