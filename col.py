from colorama import Fore, Style

def reset():
    print(Style.RESET_ALL)

def blue(message):
    if type(message) == float:
       print(Fore.BLUE,message)
    elif type(message) == int:
        print(Fore.BLUE,message)
    else:
       print(Fore.BLUE + message)


