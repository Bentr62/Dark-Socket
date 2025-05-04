import os 
import sys
import time 
import subprocess
from colorama import *



init(autoreset=False)

if sys.platform.startswith("win"):
    os.system("cls")
else:
    os.system("clear")


popup_version = "Dark'Socket v1.0"
Discord = "Bentr_62."
menu_number = 1


init(autoreset=True)

def create_banner():

    banner = f"""{Style.BRIGHT + Fore.LIGHTMAGENTA_EX}{popup_version}

                                                                                                                                                                                             
                                                                                                                                                                                        
             ██████████                       █████       ██  █████████                    █████                █████   
            ░░███░░░░███                     ░░███       ███ ███░░░░░███                  ░░███                ░░███    
             ░███   ░░███  ██████   ████████  ░███ █████░░░ ░███    ░░░   ██████   ██████  ░███ █████  ██████  ███████  
             ░███    ░███ ░░░░░███ ░░███░░███ ░███░░███     ░░█████████  ███░░███ ███░░███ ░███░░███  ███░░███░░░███░   
             ░███    ░███  ███████  ░███ ░░░  ░██████░       ░░░░░░░░███░███ ░███░███ ░░░  ░██████░  ░███████   ░███    
             ░███    ███  ███░░███  ░███      ░███░░███      ███    ░███░███ ░███░███  ███ ░███░░███ ░███░░░    ░███ ███
             ██████████  ░░████████ █████     ████ █████    ░░█████████ ░░██████ ░░██████  ████ █████░░██████   ░░█████ 
            ░░░░░░░░░░    ░░░░░░░░ ░░░░░     ░░░░ ░░░░░      ░░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░     ░░░░░  
                                                                                                                                                                                         
                                                                                                                                                                                            
                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                    By Bentr'62
                                       
                                          
                                                                                                                    
                                           
                                           {Fore.LIGHTMAGENTA_EX}Discord : {Discord}
                                           {Fore.LIGHTMAGENTA_EX}Menu Number: {menu_number}
                                           {Style.RESET_ALL}
"""
    print(banner)


    
create_banner() 
    
    




option_01 = "ddos"
option_02 = "lookup_ip"


options ={
    '01': option_01, '02' : option_02
}

choice = input(f"""{Style.BRIGHT+ Fore.LIGHTMAGENTA_EX}
                                                            ==Dark'Socket tools==

                                                            Option 1 : Ddos Tool
                                                            Option 2 : Ip Lookup 
                                                            Choississez une option (or Press q to quit) : """)
if choice in options:
    print(Style.RESET_ALL)
    script = f"Script/{options[choice]}.py"
    subprocess.run(['python', script])
elif '0' + choice in options:
    print(Style.RESET_ALL)
    script = f"Script/{options['0' + choice]}.py"
    subprocess.run(['python', script])

elif choice.lower() in ['q', 'quit']:
    print(Style.RESET_ALL)
    quit()
else:
    print("Option invalide")




