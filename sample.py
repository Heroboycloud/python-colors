import color


def greeting():
    color.green("Welcome to pythi")
    color.blue("Pick a choice : ")
greeting()
bii = color.green(input("How are you? "))
color.reset()
if bii != 5:
     color.red("oh no!")
else:
    color.yellow("nice one")
color.reset()
