import colorama
from colorama import Fore,Back , Style
colorama.init(autoreset=True)

print(Fore.WHITE + Back.RED + "White text on Red Background" )
print(Fore.YELLOW + "This is Yellow text")
print(Fore.GREEN + Back.WHITE + "Green text on White")
print("Default text")
print(Style.BRIGHT + "Bright text")