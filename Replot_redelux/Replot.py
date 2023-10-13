#This is the shittist program you ever read

#No comments

#Strange mechanisms Warning

import glob , os , cv2

def terminalMode():

    print("          _____                    _____                    _____                    _____           _______               _____           ")
    print("         /\    \                  /\    \                  /\    \                  /\    \         /::\    \             /\    \          ")
    print("        /::\    \                /::\    \                /::\    \                /::\____\       /::::\    \           /::\    \         ")
    print("       /::::\    \              /::::\    \              /::::\    \              /:::/    /      /::::::\    \          \:::\    \        ")
    print("      /::::::\    \            /::::::\    \            /::::::\    \            /:::/    /      /::::::::\    \          \:::\    \       ")
    print("     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /      /:::/~~\:::\    \          \:::\    \      ")
    print("    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/    /      /:::/    \:::\    \          \:::\    \     ")
    print("   /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/    /      /:::/    / \:::\    \         /::::\    \    ")
    print("  /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    /      /:::/____/   \:::\____\       /::::::\    \   ")
    print(" /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/    /      |:::|    |     |:::|    |     /:::/\:::\    \  ")
    print("/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/____/       |:::|____|     |:::|    |    /:::/  \:::\____\ ")
    print("\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\::/    \:::\  /:::|____|\:::\    \        \:::\    \   /:::/    /    /:::/    \::/    / ")
    print(" \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \/_____/\:::\/:::/    /  \:::\    \        \:::\    \ /:::/    /    /:::/    / \/____/  ")
    print("       |:::::::::/    /    \:::\   \:::\    \               \::::::/    /    \:::\    \        \:::\    /:::/    /    /:::/    /           ")
    print("       |::|\::::/    /      \:::\   \:::\____\               \::::/    /      \:::\    \        \:::\__/:::/    /    /:::/    /            ")
    print("       |::| \::/____/        \:::\   \::/    /                \::/____/        \:::\    \        \::::::::/    /     \::/    /             ")
    print("       |::|  ~|               \:::\   \/____/                  ~~               \:::\    \        \::::::/    /       \/____/              ")
    print("       |::|   |                \:::\    \                                        \:::\    \        \::::/    /                             ")
    print("       \::|   |                 \:::\____\                                        \:::\____\        \::/____/                              ")
    print("        \:|   |                  \::/    /                                         \::/    /         ~~                                    ")
    print("         \|___|                   \/____/                                           \/____/                                                ")
    print("                                                                                                                                           ")

    while True:
        
        print("\nTerminal :")

        mode = ""
        mode = input()
        mode = mode.lower()

        if mode == "help":

            print("plt     - Normal plot mode")
            print("pltx    - Only plot X value in image")
            print("plty    - Only plot Y value in image")
            print("plotcpt - Use PlotChiPT AI model to plot image (Only for JetBot) --- WIP")
            print("quit    - Quit program")
        
        elif mode == "plt":

            pltMode()
        
        elif mode == "pltx":

            pass

        elif mode == "plty":

            pass

        elif mode == "quit":

            quit()

def jbORjr(name):
    if name[0] == "x":
        return "jb"
    else:
        return "jr"
    
def pltMode():
    
    print("File path?")

    path = str(input())

    try:
        os.chdir(path)
    except BaseException:
        pass

    imgs_arr = glob.glob("*.jpg")

    if jbORjr(imgs_arr[0]) == "jb":
        pass
    else:
        pass
    
    pass

terminalMode()