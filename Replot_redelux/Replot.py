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

        for i in tqdm.tqdm(range(len(imgs_arr))):
            
            Out = pltjb("both" , imgs_arr[i])

            if Out == -2:
                
                i -= 1
            
            else:
                
                os.rename(imgs_arr[i] , Out)
                imgs_arr[i] = Out
            
        
        cv2.destroyAllWindows()

    else:
        pass
    
    pass

def pltjb(xORyOrBoth , name):
 
    global mouseX , mouseY , stat , ori_img , img

    stat = -3

    #find xy
    x , y = "" , ""

    x += name[3] + name[4] + name[5]
    y += name[7] + name[8] + name[9]

    x = int(x)
    y = int(y)

    def click_event(event , x , y , flags ,param):

        global mouseX , mouseY , stat

        if event == cv2.EVENT_LBUTTONDOWN:

            mouseX = x
            mouseY = y
            stat = -1
            
            cv2.imshow("Replot" , cv2.circle(cv2.imread(name) , (x ,y) , 8 , (0,255,0) , 3))

        elif event == cv2.EVENT_RBUTTONDOWN:

            stat = -2

    ori_img = cv2.imread(name)
    img = cv2.circle(ori_img , (x ,y) , 8 , (0,255,0) , 3)
    cv2.imshow("Replot" , img)

    cv2.setMouseCallback("Replot" , click_event)
    key = cv2.waitKey(0)
    
    if stat == -1:
        
        newXY = [("%03d" %mouseX) , ("%03d" %mouseY)]

        nameList = []

        for i in name:
            nameList.append(i)
        
        if xORyOrBoth == "x" or xORyOrBoth == "both":

            nameList[3] , nameList[4] , nameList[5] = newXY[0][0] , newXY[0][1] , newXY[0][2]

        if xORyOrBoth == "y" or xORyOrBoth == "both":

            nameList[7] , nameList[8] , nameList[9] = newXY[1][0] , newXY[1][1] , newXY[1][2]

        name = "".join(nameList)

        return name

    if stat == -2:

        return -2

    if stat == -3:
        
        return name

terminalMode()