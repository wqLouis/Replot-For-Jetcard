from plot_library import *
import glob , cv2 , os
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
    if event == cv2.EVENT_RBUTTONDBLCLK:
        global i
        i -= 2
        cv2.destroyAllWindows()
def click_event_bot(event , x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        name = filelist[pos]
        posx , posy = [] , []
        for cord in str(x):
            posx.append(cord)
        for cord in str(y):
            posy.append(cord)
        posx , posy = shifting(str(x) , 3) , shifting(str(y) , 3)
        new_name = edit_name(name,posx,posy,3,3,7)
        os.rename(name , new_name)
        filelist[pos] = new_name
        print("New name : "+new_name)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        global i
        i -= 2
        cv2.destroyAllWindows()
def ask(qus):
    print(qus)
    inp = input()
    if len(inp) != 0:
        return inp
def plot_jetbot():
    name = filelist[i]
    global pos
    pos = i
    x = get_current_xy(name , 3 , 3) 
    y = get_current_xy(name , 3 , 7)
    img = cv2.imread(name , cv2.IMREAD_UNCHANGED)
    global new_img
    new_img = img
    draw_img(img , int(x) , int(y))
    img = draw_line(4 , img)
    cv2.imshow("Img -JetBot" , img)
    cv2.setMouseCallback("Img -JetBot" , click_event_bot)
    cv2.waitKey(0)
    if key == ord("q"):
        print("Are you sure to leave this program? [y/n]")
        key = cv2.waitKey(0)
        if key == ord("y"):
            print("Exit program")
            exit()
        elif key == ord("n"):
            del(key)
            print("Exit program canceled")
def plot_racer():
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
    key = cv2.waitKey(0)
    if key == ord("q"):
        print("Are you sure to leave this program? [y/n]")
        key = cv2.waitKey(0)
        if key == ord("y"):
            print("Exit program")
            exit()
        elif key == ord("n"):
            del(key)
            print("Exit program canceled")

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
        return "jr"
    if ans == "jb":
        return "jb"
i = 0
key = 0
mode = main()
if __name__ =="__main__" :
    if mode == "jb":
        while True:
            plot_jetbot()
            i += 1
            if i >= len(filelist):
                break
            else:
                progress_bar(i , len(filelist) , 20)
    elif mode == "jr":
        while True:
            plot_racer()
            i += 1
            if i >= len(filelist) or key == ord("q"):
                print("Finished !")
                break
            else:
                progress_bar(i , len(filelist) , 20)