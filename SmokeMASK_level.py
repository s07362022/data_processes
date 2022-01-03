import cv2 
import numpy as np
import os
import math
import plotly.graph_objects as go
import time
from PIL import Image
t_prev = time.time()
h_min = 30
s_min = 0
v_min = 0
h_max = 179
s_max = 179
v_max = 129

#path = 'E:\\workspace\\project_\\file_smoke\\smoke_0.png'
#img = cv2.imread(path)
#img = cv2.resize(img,(400,400))
#imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#lower=np.array([h_min,s_min,v_min])
#upper=np.array([h_max,s_max,v_max])
#mask=cv2.inRange(imgHSV,lower,upper)
#imgResult = cv2.bitwise_and(img,img,mask=mask)


#色溫
kelvin_table = {
    1000: (255,56,0),
    1500: (255,109,0),
    2000: (255,137,18),
    2500: (255,161,72),
    3000: (255,180,107),
    3500: (255,196,137),
    4000: (255,209,163),
    4500: (255,219,186),
    5000: (255,228,206),
    5500: (255,236,224),
    6000: (255,243,239),
    6500: (255,249,253),
    7000: (245,243,255),
    7500: (235,238,255),
    8000: (227,233,255),
    8500: (220,229,255),
    9000: (214,225,255),
    9500: (208,222,255),
    10000: (204,219,255)}
def convert_temp(image, temp):
    r, g, b = kelvin_table[temp]
    matrix = ( r / 255.0, 0.0, 0.0, 0.0,
               0.0, g / 255.0, 0.0, 0.0,
               0.0, 0.0, b / 255.0, 0.0 )
    return image.convert('RGB', matrix)

def tem(img):   
    img2= Image.fromarray(np.uint8(img))
    w = convert_temp(img2,4500)
    img = np.asarray(w)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    return mask
#MASK
def mask_img(mask):
    g = np.zeros((mask.shape[0],mask.shape[1]))
    i_list = []
    k_list = []
    #print(mask.shape)
    for i in range (mask.shape[0]):
        for k in range(mask.shape[1]):
            if mask[i][k] != 0:
                g[i][k] = 1
                i_list.append(i)
                k_list.append(k)
       
    #print("max_h=",max(i_list),"mix_h=",min(i_list))
    #print("max_w=",max(k_list),"mix_w=",min(k_list))
    h_pix = min(i_list) - 100
    smoke_1 = img[h_pix:min(i_list),min(k_list):max(k_list)]
    #print(smoke_1.shape)
    mask_1 = g[h_pix:max(i_list),min(k_list):max(k_list)]
    mask_2 = g[h_pix:min(i_list),min(k_list):max(k_list)]
    return smoke_1,mask_2

#初始化
def leavel(black,ori):
    black_h,black_w = black.shape[0] ,  black.shape[1]
    level_s = [[255,255,255],[209,210,212],[167,169,172],[129,130,133],[88,88,90],[35,31,32]] ## 林格曼標籤分級
    res = [0] * 6 

    for i in range(black_h): ##訪問每個像素
        for j in range(black_w):
            if black[i][j] >= 0 :  ###  背景
                level_s2,d = 0 , 1000000000000000000000             ##不是背景  判斷哪一級
                for z in range(len(level_s)):
                    std_d = (abs( ori[i][j][0] -level_s[z][0] )**2+abs( ori[i][j][1] -level_s[z][1] )**2+abs( ori[i][j][2] -level_s[z][2] )**2)**0.5
                    if  std_d < d:
                            d,level_s2 = std_d,z
                res[level_s2] = res[level_s2] + 1
                #print(res)
    #print('此照片不透視率 %s 級 有 %s 個  , 比例為 %s ' %   ( res.index(max(res)) , max(res) , round(max(res) / sum(res),2) * 100 ) )
    return res.index(max(res))


#DataPath
all_files = []
all_paths = []
for path, dir, file in os.walk("E:\\workspace\\project_\\file_smoke\\"): #資料夾路徑
    for f in file:
        if os.path.splitext(f)[-1] in ['.png']:
            all_files.append(f)
            all_paths.append(path)

#Mask and Leavel
leavel_list = []
for k in range (len(all_files)):
    img = cv2.imread(all_paths[k]+ all_files[k])
    ####使用色溫調整############
    #mask = tem(img)
    #imgResult = cv2.bitwise_and(img,img,mask=mask)
    #######################
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    #imgResult = cv2.bitwise_and(img,img,mask=mask)
    ori,black  = mask_img(mask)
    leavel_list.append(leavel(black,ori))

#print(leavel_list[:10])
level_mean = np.mean(leavel_list)
level_var = np.var(leavel_list,ddof=1)
level_std = np.std(leavel_list,ddof=1)
print("mean=",level_mean,"variance=",level_var)

def normal_distribution(x, mean, var):
    return np.exp(-1*(abs(x-mean)**2)/(2*(var)))/(math.sqrt(2*np.pi) * (level_std))

x1 = np.linspace(level_mean - 6*level_std, level_mean + 6*level_std, 100)
ll=np.array(leavel_list)
x2 = np.linspace(1,6,6)
y2 = [np.count_nonzero(ll==1),np.count_nonzero(ll==2),np.count_nonzero(ll==3),np.count_nonzero(ll==4),np.count_nonzero(ll==5),np.count_nonzero(ll==6)]
y2=np.array(y2)
print(x2,y2)
def draw(x1,y1):
    trace0 = go.Scatter(
        x=x1,
        y=y1,
        mode='markers',#+text
        name="normal_distribution",
        text=y1,
        textposition="top left",
        hovertemplate="<b>%{x}</b> 平均級別<br><b>%{y}</b> 常態分布級別",
    )
    fig = go.Figure([trace0])
    fig.update_layout(
        title_text='排放廢氣煙霧之等級畫分',
        title_font_size=30,
        title_x=0.5,
        xaxis_title="常態分布",
        xaxis_tickmode="linear",
        yaxis_title="等級",
        showlegend=True,
    )
    fig.show()
def draw2(x2,y2):
    trace1 = go.Bar(
            x=x2,
            y=y2,
            #+text,mode='markers'
            name="Bar",
            text=y2,
            textposition="outside",
            hovertemplate="<b>%{x}</b> 級別類別<br><b>%{y}</b> 等級",
        )
    fig = go.Figure([trace1])
    fig.update_layout(
        title_text='排放廢氣煙霧之等級畫分',
        title_font_size=30,
        title_x=0.5,
        xaxis_title="級別類別",
        xaxis_tickmode="linear",
        yaxis_title="等級",
        showlegend=True,
    )
    fig.show()    

if float(level_var) != 0.0:

    y1 = normal_distribution(x1,level_mean,level_var)
    over_time = int((time.time()-t_prev))
    print("花費 cost time:",over_time,"s")
    draw(x1,y1)
    draw2(x2,y2)
else :
    print("測出的資料都一樣: {} 級".format(level_mean))
#print(type(leavel_list))
