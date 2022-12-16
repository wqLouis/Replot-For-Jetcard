import cv2 , glob , os
def find_jpg(file_path):
    tem_list = []
    file_path = file_path.replace("\\" , "/")
    os.chdir(file_path)
    tem_list = glob.glob("*.jpg")
    return tem_list
def draw_img(img , x ,y):
    img = cv2.circle(img , (x ,y) , 8 , (0,255,0) , 3)
    return img
def shift(target_len , var):
    tem_list = []
    for i in range(target_len - len(var)):
        tem_list.append("0")
    for i in var:
        tem_list.append(i)
    return tem_list
def show_img(file_path):
    img = cv2.imread(file_path , cv2.IMREAD_UNCHANGED)
    cv2.imshow("Img" , img)
    cv2.waitKey(0)
def newname(old , var , startvar , len):
    tem_list , tem_str= [] , ""
    for i in old:
        tem_list.append(i)
    for i in range(len):
        tem_list[i+startvar] = var[i]
    tem_str = "".join(tem_list)
    return tem_str
def get_current_xy(file_name , len , startvar):
    tem_list = []
    var = ""
    for i in file_name:
        tem_list.append(i)
    for i in range(len):
        var += tem_list[i+startvar]
    return var
def lenofName(name , startvar , endstr):
    tem_list = []
    pos = 0
    for i in name:
        tem_list.append(i)
    for i in range(10):
        if tem_list[i+startvar] == endstr:
            return pos
        else:
            pos+=1
def rename_jetracer(name , var , varlen , startvar):
    tem_list = []
    var_list = []
    tem_str = ""
    tem_int = 0
    for i in name:
        tem_list.append(i)
    for i in range(varlen):
        tem_list.pop(startvar)
    for i in var:
        var_list.append(i)
    var_list.reverse()
    for i in var_list:
        tem_list.insert((startvar) , i)
        tem_int += 1
    tem_str = "".join(tem_list)
    return tem_str
def shifting(xy_list,xy_len):
    xy_list=str(xy_list)
    tem_xylist=[]
    for i in xy_list:
        tem_xylist.append(i)
    tem_list=[]
    starting_pos=0
    starting_pos=(xy_len-(len(tem_xylist)))
    for i in range(starting_pos):
        tem_list.append("0")
    for i in tem_xylist:
        tem_list.append(i)
    return tem_list
def edit_name(img_name,x,y,xy_len,start_x,start_y):
    tem_list=[]
    tem_str=""
    for i in img_name:
        tem_list.append(i)
    for i in range(xy_len):
        tem_list[(start_x)+i]=x[i]
    for i in range(xy_len):
        tem_list[(start_y)+i]=y[i]
    tem_str="".join(tem_list)
    return tem_str
def draw_line(NumLine , img):
    height , width = img.shape[0] , img.shape[1]
    NewLine = width/NumLine
    for i in range(NumLine):
        img = cv2.line(img , (int(NewLine*i) , height) , (int(NewLine*i) , 0) , (0,0,0) , 2)
    return img
def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)
