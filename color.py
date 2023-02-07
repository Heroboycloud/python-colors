from colorama import Fore,Back, Style
# this program is module huh....

def green(message):
    message = str(message)
    print(Fore.GREEN + message)


def blue(message):
    message = str(message)
    print(Fore.BLUE + message)


def yellow(message):
    message = str(message)
    print(Fore.YELLOW + message)


def gray(message):
    message = str(message)
    print(Fore.GRAY + message)


def red(message):
    message = str(message)
    print(Fore.RED + message)


def note(message):
    message = str(message)
    print(message + "......")


def magenta(message):
    message = str(message)
    print(Fore.MAGENTA + message)


def cyan(message):
    message = str(message)
    print(Fore.CYAN + message)

def reset():
    print(Style.RESET_ALL)