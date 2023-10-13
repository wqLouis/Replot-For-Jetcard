#This is the shittist program you ever read

#No comments

#Strange mechanisms Warning

import glob , os , cv2 , tqdm

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
        
        else:
            print("Unknown command - type help for help")

def jbORjr(name):
    if name[0] == "x":
        return "jb"
    else:
        return "jr"
    
def pltMode():
    
    print("File path?")

    path = str(input())

    if not(os.getcwd() == path):
        try:
            os.chdir(path)
        except BaseException:
            print("Error when changing directory - Maybe try again?")

    imgs_arr = glob.glob("*.jpg")

    if len(imgs_arr) == 0:
        
        print("Empty Directory :-(")
        return

    if jbORjr(imgs_arr[0]) == "jb":

        for i in tqdm(range(len(imgs_arr))):
            
            imgs_arr[i] = pltjb("both" , imgs_arr[i])

    else:
        pass
    
    pass

def pltjb(xORyOrBoth , name):

    #find xy
    x , y = "" , ""

    x += name[3] + name[4] + name[5]
    y += name[7] + name[8] + name[9]

    x = int(x)
    y = int(y)

    cv2.imread()

terminalMode()