from plot_library import *
import glob , cv2 , os
#path = "C:/Users/Student/OneDrive/桌面/JetBot/Garbage/dataset2/apex/"
#filelist = find_jpg(path)
def click_event_racer(event , x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global new_img
        name = filelist[pos]
        posx = lenofName(name , 0 , "_")
        new_name = rename_jetracer(name , str(x) , posx , 0)
        posx_new = lenofName(new_name , 0 , "_")
        posy_new = lenofName(new_name , (posx_new+1) , "_")
        new_name = rename_jetracer(new_name , str(y) , posy_new , (posx_new+1))
        os.rename(name , new_name)
        filelist[pos] = new_name
        print("New name : "+new_name)
def click_event_bot(event , x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        name = filelist[pos]
        posx , posy = [] , []
        for i in str(x):
            posx.append(i)
        for i in str(y):
            posy.append(i)
        posx , posy = shifting(str(x) , 3) , shifting(str(y) , 3)
        new_name = edit_name(name,posx,posy,3,3,7)
        os.rename(name , new_name)
        filelist[pos] = new_name
        print("Name name : "+new_name)
def ask(qus):
    print(qus)
    inp = input()
    if len(inp) != 0:
        return inp
def plot_jetbot():
    for i in range(len(filelist)):
        name = filelist[i]
        global pos
        pos = i
        print(name)
        x = get_current_xy(name , 3 , 3) 
        y = get_current_xy(name , 3 , 7)
        img = cv2.imread(name , cv2.IMREAD_UNCHANGED)
        global new_img
        new_img = img
        draw_img(img , int(x) , int(y))
        cv2.imshow("Img -JetBot" , img)
        cv2.setMouseCallback("Img -JetBot" , click_event_bot)
        cv2.waitKey(0)
def plot_racer():
    for i in range(len(filelist)):
        name = filelist[i]
        global pos
        pos = i
        posx = lenofName(name , 0 , "_")
        posy = lenofName(name , (posx+1) , "_")
        current_x = get_current_xy(filelist[i] , posx , 0)
        current_y = get_current_xy(filelist[i] , posy , posx+1)
        img = cv2.imread(filelist[i] , cv2.IMREAD_UNCHANGED)
        draw_img(img , int(current_x) ,int(current_y))
        cv2.imshow("Img -JetRacer" , img)
        cv2.setMouseCallback("Img -JetRacer" , click_event_racer)
        cv2.waitKey(0)
def main():
    global path
    path = ask("Path :")
    path = path.replace("\\" , "/")
    tem_list = []
    for i in path:
        tem_list.append(i)
    tem_list.reverse()
    if tem_list[0] != "/":
        path += "/"
    try:
        find_jpg(path)
    except BaseException:
        print("Syntax Error")
        return 0
    else:
        global filelist
        filelist = find_jpg(path)
    ans = ask("Mode for plot [jb/jr] :")
    if ans == "jr":
        plot_racer()
    if ans == "jb":
        plot_jetbot()
if __name__ =="__main__" :
    while True:
        main()
