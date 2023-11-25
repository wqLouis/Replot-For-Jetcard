#This is the shittist program you ever read

#No comments

#Strange mechanisms Warning

try:
    import cv2
except BaseException:
    print("Cannot import library CV2 check if it is installed \n Press any key to quit")
    input()
    quit()

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

            pltMode("both")
        
        elif mode == "pltx":

            pltMode("x")

        elif mode == "plty":

            pltMode("y")

        elif mode == "quit":

            quit()
        
        else:
            print("Unknown command - type help for help")

def jbORjr(name):
    if name[0] == "x":
        return "jb"
    else:
        return "jr"
    
def pltMode(xymode):
    
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

        for i in range(len(imgs_arr)):
            
            Out = pltjb(xymode , imgs_arr[i])
                
            if Out == 0:
                break

            os.rename(imgs_arr[i] , Out)
            imgs_arr[i] = Out
        
        cv2.destroyAllWindows()

    else:
        
        for i in range(len(imgs_arr)):

            Out = pltjr(xymode , imgs_arr[i])

            if Out == 0:
                break
            
            os.rename(imgs_arr[i] , Out)
            imgs_arr[i] = Out

        cv2.destroyAllWindows()
    
    pass

def pltjb(xORyOrBoth , name):
 
    global mouseX , mouseY , ori_img , img , oriXY

    mouseX , mouseY = 0 , 0

    #find xy
    x , y = "" , ""

    x += name[3] + name[4] + name[5]
    y += name[7] + name[8] + name[9]

    x = int(x)
    y = int(y)

    oriXY = [x , y]

    def click_event(event , x , y , flags ,param):

        global mouseX , mouseY , oriXY

        if event == cv2.EVENT_LBUTTONDOWN:

            if xORyOrBoth == "x" or xORyOrBoth == "both":
                mouseX = x
            else:
                mouseX = oriXY[0]

            if xORyOrBoth == "y" or xORyOrBoth == "both":
                mouseY = y
            else:
                mouseY = oriXY[1]
            
            cv2.imshow("Replot" , cv2.circle(cv2.imread(name) , (mouseX ,mouseY) , 8 , (0,255,0) , 3))

    ori_img = cv2.imread(name)
    img = cv2.circle(ori_img , (x ,y) , 8 , (0,255,0) , 3)
    cv2.imshow("Replot" , img)

    cv2.setMouseCallback("Replot" , click_event)
    key = cv2.waitKey(0)

    if key == ord("q"):
        return 0
        
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

def pltjr(xORyOrBoth , name):

    global mouseX , mouseY
    
    num_1 , num_2 , number_ = 0 , 1 , 0

    ori_img = cv2.imread(name)
    img = ori_img.copy()

    for i in name:
        if i == "_":
            number_ += 1
            if number_ == 2:
                break
        if i != "_":
            if number_ == 0:
                num_1 += 1
            num_2 += 1
        
    x , y = "" , ""

    for i in range(num_1):
        x += name[i]
    for i in range(num_1 + 1 , num_2):
        y += name[i]

    x , y = int(x) , int(y)
    mouseX , mouseY = x , y
    oriXY = [x , y]

    img = cv2.circle(ori_img.copy() , (x ,y) , 8 , (0,255,0) , 3)
    img = cv2.line(img , (0 , 112) , (224 , 112) , (0,0,0) , 1)
    img = cv2.line(img , (0 , 179) , (224 , 179) , (0,0,0) , 1)
    img = cv2.line(img , (112 , 0) , (112 , 224) , (0,0,0) , 1)
    
    def click_event(event , x , y , flags ,param):

        global mouseX , mouseY

        if event == cv2.EVENT_LBUTTONDOWN:

            if xORyOrBoth == "x" or xORyOrBoth == "both":
                mouseX = x

            if xORyOrBoth == "y" or xORyOrBoth == "both":
                mouseY = y
            
            clied_img = cv2.circle(ori_img.copy() , (x ,y) , 8 , (0,255,0) , 3)
            clied_img = cv2.line(clied_img , (0 , 112) , (224 , 112) , (0,0,0) , 1)
            clied_img = cv2.line(clied_img , (0 , 179) , (224 , 179) , (0,0,0) , 1)
            clied_img = cv2.line(clied_img , (112 , 0) , (112 , 224) , (0,0,0) , 1)

            cv2.imshow("Replot" , clied_img)

    cv2.imshow("Replot" , img)
    cv2.setMouseCallback("Replot" , click_event)

    key = cv2.waitKey(0)

    if key == ord("q"):
        return 0

    newXY = [mouseX , mouseY]
    nameList = []

    for i in name:
        nameList.append(i)

    for i in range(num_1):
        nameList.pop(0)

    for i in range(num_2-num_1-1):
        nameList.pop(1)
    
    if xORyOrBoth == "y" or xORyOrBoth == "both":
        for i in range(len(str(newXY[1]))):
            nameList.insert(1+i , str(newXY[1])[i])
    if xORyOrBoth == "x" or xORyOrBoth == "both":
        for i in range(len(str(newXY[0]))):
            nameList.insert(i , str(newXY[0])[i])

    name = "".join(nameList)
    
    return name

terminalMode()