import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC']
global situation_list
global gap_list

data1 = pd.read_excel("D:\\traffic\臺中市政府警察局108年1月份交通事故資料.XLSX")
data2 = pd.read_excel("D:\\traffic\臺中市政府警察局108年2月份交通事故資料.XLSX")
data3 = pd.read_csv("D:\\traffic\臺中市政府警察局108年3月份交通事故資料.csv")
data4 = pd.read_excel("D:\\traffic\臺中市政府警察局108年4月份交通事故資料.XLSX")
data5 = pd.read_excel("D:\\traffic\臺中市政府警察局108年5月份交通事故資料.XLSX")
data6 = pd.read_excel("D:\\traffic\臺中市政府警察局108年6月份交通事故資料.XLSX")
data7 = pd.read_csv("D:\\traffic\臺中市政府警察局108年7月份交通事故資料.csv")
data8 = pd.read_csv("D:\\traffic\臺中市政府警察局108年8月份交通事故資料.csv")

print('路面狀況與路面鬆軟造成事故的件數統計')
print('\n')
#第一
road1 = data1[['路面狀態','路面缺陷']] #,'路面缺陷'
road1 = road1.fillna(0)
all1 = data1['年']
fact1 = data1[['肇事因素個別','肇事因素主要']]
#第二
road2 = data2[['路面狀態','路面缺陷']] #,'路面缺陷'
road2 = road2.fillna(0)
all2 = data2['年']
fact2 = data2[['肇事因素個別','肇事因素主要']]
#第三
road3 = data3[['路面狀態','路面缺陷']] #,'路面缺陷'
road3 = road3.fillna(0)
all3 = data3['年']
fact3 = data3[['肇事因素個別','肇事因素主要']]
#第四
road4 = data4[['路面狀態','路面缺陷']] #,'路面缺陷'
road4 = road4.fillna(0)
all4 = data4['年']
fact4 = data4[['肇事因素個別','肇事因素主要']]
#第五
road5 = data5[['路面狀態','路面缺陷']] #,'路面缺陷'
road5 = road5.fillna(0)
all5 = data5['年']
fact5 = data5[['肇事因素個別','肇事因素主要']]
#第六
road6 = data6[['路面狀態','路面缺陷']] #,'路面缺陷'
road6 = road6.fillna(0)
all6 = data6['年']
fact6 = data6[['肇事因素個別','肇事因素主要']]
#第七
road7 = data7[['路面狀態','路面缺陷']] #,'路面缺陷'
road7 = road7.fillna(0)
all7 = data7['年']
fact7 = data7[['肇事因素個別','肇事因素主要']]
#第八
road8 = data8[['路面狀態','路面缺陷']] #,'路面缺陷'
road8 = road8.fillna(0)
all8 = data8['年']
fact8 = data8[['肇事因素個別','肇事因素主要']]

'''
#合併8個資料
#pd.concat([], axis=0)
#pd.concat([], axis=1)
'''
concat = pd.concat([road1, road2, road3, road4, road5, road6, road7, road8], axis=0)
concat_all = pd.concat([all1,all2,all3,all4,all5,all6,all7,all8])
concat_fact = pd.concat([fact1,fact2,fact3,fact4,fact5,fact6,fact7,fact8], axis=0)
 #個別資料
#situation = data1['路面狀態']
#situation = situation.dropna()
#gap = data1['路面缺陷']
#gap = gap.dropna()

#統計
 #value_situation = situation.value_counts()
 #print (value_situation)
 #print("\n")
gap = all_gap = concat['路面缺陷']
value_gap = gap.value_counts()
all_situation = concat['路面狀態']
all_gap = concat['路面缺陷']
 #print (value_gap)
fact_single = concat_fact['肇事因素個別']
##fact_main = concat_fact['肇事因素主要']
value_fact_single = fact_single.value_counts()
##value_fact_main = fact_main.value_counts()
 #print(value_fact_single)
 #print(value_fact_main)

#統計數字
 ##路況危險無安全(警告)設施 18
 #print(concat_all)
 ##總數67216
 ##路面缺陷107+無資料24939

def load_situation():
    global all_situation
    global situation_list
    input1 = ''
    print('路面狀況:1:冰雪，2:油滑，3:泥濘，4:濕潤，5:乾燥')
    all_situation = concat['路面狀態']
 #print(all_situation)
    situation_count = all_situation.value_counts()
    for i in range(100):
        input1 = input('請選擇狀況編號查看件數,選擇離開請輸入6,選擇全部請按0:')
        if input1 == '1':
            print('路面冰雪8件')
        elif input1 == '2':
            print('路面油滑18件')
        elif input1 == '3':
            print('路面泥濘20件')
        elif input1 == '4':
            print('路面濕潤4609件')
        elif input1 == '5':
            print('路面枯燥25704件')
        elif input1 == '6':
            break
        elif input1 == '0':
            print('根據調查:','\n','路面枯燥25704件','\n','路面濕潤4609件','\n','路面泥濘20件','\n','路面油滑18件','\n','路面冰雪8件')       
        else :
            print('Error,please choise another options')
situation_list = [25704, 4609, 20, 18, 8]

#print(situation_count)
#print('根據調查:','\n','路面枯P燥25704件','\n','路面濕潤4609件','\n','路面泥濘20件','\n','路面油滑18件','\n','路面冰雪8件')
print('\n')

##路面缺陷
def load_gap():
    global all_gap
    global gap_list
    print('1:路面鬆軟，2:突出(高低)不平，3:有坑洞，4:無缺陷')
    input2 = ''
    all_gap = concat['路面缺陷']
    gap_count = all_gap.value_counts()
    for i in range(100):
        input2 = input('請選擇狀況編號查看件數,選擇離開請輸入6,選擇全部請按0:')
        if input2 == '1':
            print('路面鬆軟25件')
        elif input2 == '2':
            print('突出(高低)不平38件')
        elif input2 == '3':
            print('有坑洞44件')
        elif input2 == '4':
            print('無缺陷30245件')
        elif input2 == '6':
            break
        elif input2 == '0':
            print('根據調查:','\n','無缺陷30245件','\n','有坑洞44件','\n','突出(高低)不平38件','\n','路面鬆軟25件')       
        else :
            print('Error,please choise another options')
gap_list = [30245, 44, 38, 25]
#print(gap_count)
#print('根據調查:','\n','無缺陷30245件','\n','有坑洞44件','\n','突出(高低)不平38件','\n','路面鬆軟25件')

####main().....................................................................

##畫圖
def load_situation_plt():
    plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC']
    bar_width = 0.3
    index = np.arange(len(situation_list))
    load_situation_plt = plt.bar(index, situation_list,bar_width,alpha=0.5,label="situation")
    def createLabels(data):
        for item in data:
            height = item.get_height()
            plt.text(
                item.get_x()+item.get_width()/2., 
                height*1.05, 
                '%d' % int(height),
                ha = "center",
                va = "bottom",)
    createLabels(load_situation_plt)
 # 定義標籤
    plt.ylabel("件數")          # 設定y軸標題 
    plt.xlabel("狀況種類")            # 設定x軸標題
    plt.title("路面狀況")
    plt.xticks(index + .1, ("路面枯燥","路面濕潤","路面泥濘","路面油滑","路面冰雪8件"))
    plt.ylim(0,26000)
 #    plt.plot(2,3,label="") #圖例
    plt.grid(True)
    plt.show()
##load_situation_plt()

def load_gap_plt():
    plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC']
    bar_width = 0.3
    index = np.arange(len(gap_list))
    load_gap_plt = plt.bar(index, gap_list,bar_width,alpha=0.5,label="gap")
    def createLabels(data):
        for item in data:
            height = item.get_height()
            plt.text(
                item.get_x()+item.get_width()/2., 
                height*1.05, 
                '%d' % int(height),
                ha = "center",
                va = "bottom",)
    createLabels(load_gap_plt)
 # 定義標籤
    plt.ylabel("件數")          # 設定y軸標題 
    plt.xlabel("缺陷種類")            # 設定x軸標題
    plt.title("路面缺陷")
    plt.xticks(index + .1, ("無缺陷","有坑洞","突出(高低)不平","路面鬆軟"))
    plt.ylim(0,30500)
 #    plt.plot(2,3,label="") #圖例
    plt.grid(True)
    plt.show()
 #load_gap_plt()


##路面缺陷107+無資料24939 ##總數55291 #有資料30352
real_gap_percent = 107 / 30352*100
#print(real_gap_percent) #路面缺陷占0.3%
fake_gap_percent = 30245 / 30352 * 100
#print(fake_gap_percent) #路面無缺陷占99.6%

##畫圖(圓餅圖)
def gap_percent():
    x = (real_gap_percent,fake_gap_percent)
    labels = ['因路面缺陷發生事故','無缺陷發生事故']
    plt.pie(x,labels=labels,autopct='%1f%%',shadow=False,startangle=100)
    plt.show()

#路況危險無安全(警告)設施統計
def nonotice():
    percent_nonotice = 18 / 107 *100
    percent_notice = (107-18) / 107 *100
    z = (percent_nonotice,percent_notice)
    label = ['無安全(警告)設施','有安全(警告)設施']
    plt.pie(z,labels=label,autopct='%1f%%',shadow=False,startangle=100)
    plt.show()


def accident_fact_five(): #肇事主要因素concat['路面缺陷']
    #traffic_108=concat_fact['肇事因素主要']
    #traffic_108= fact_main
    #traffic_108=traffic_108.dropna(axis=0, how='any' )
    #traffic_108_count =traffic_108.groupby()#"肇事因素主要"
    #traffic_108_count.size()
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.xticks(fontsize=13) #x標籤字體大小
#font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
    plt.xticks(rotation=70)  # 设置横坐标显示的角度，角度是逆时针，自己看
    tick_spacing = 3 # 设置密度，比如横坐标9个，设置这个为3,到时候横坐标上就显示 9/3=3个横坐标
    x = ['6', '23', '43', '26', '42']
    count_a = [7526, 7264, 1888, 1879, 1820]
    plt.bar(x, count_a, label = 'count_a', color = 'royalblue')
    plt.ylabel ('肇事數量')#y軸標標籤
    plt.title('108五大肇事因素')
    plt.xticks(range(5),['未依規定讓車','未注意車前狀態','不明原因肇事','違反特定標誌(線)禁制 ','未保持行車安全距離'])
    for x,y in enumerate(count_a):
        plt.text(x,y+100,'%s' %y,ha='center')
    plt.show()

def accident_fact_pie():
    x = ['未依規定讓車','未注意車前狀態','不明原因肇事','違反特定標誌(線)禁制 ','其他引起事故之違規或不當行為','其他肇事原因']
    traffic_c = [7526, 7264, 1888, 1879, 1820,14291]
    plt.pie(traffic_c)
    pie_color = ["cornflowerblue","plum", "grey", "peru", "yellowgreen","khaki"]
    explode_p = (0.1, 0, 0, 0, 0,0)
    plt.pie(traffic_c, colors = pie_color, labels = x, autopct = "%2.2f%%", explode=explode_p)
    plt.title("108肇事因素比例")
    plt.show()


def accident_fact_compare():
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  #用来正常显示中文标签
    #plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.figure(figsize=(10, 8))
    plt.xticks(fontsize=13) #x標籤字體大小
    col_count =6                  # 由於有3個月，設定類別基數為3
    bar_width = 0.2                # 設定長條圖每個長條寬度
    index = np.arange(col_count)   # 依據3個類別(3個月)設定索引值，便於後續長條圖的位置設定
    #font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12) #设置横坐标显示的角度，角度是逆时针，自己看
    plt.xticks(range(6),['未依規定讓車','未注意車前狀態','未保持行車安全距離','違反特定標誌(線)禁制 ','違反號誌管制或指揮','不明原因肇事'])
    x = ['未依規定讓車', '未注意車前狀態', '未保持行車安全距離', '違反特定標誌(線)禁制', '違反號誌管制或指揮','不明原因肇事']
    count_106 = [16367, 15082, 4388, 4037, 4018,3806]
    count_107 = [10848, 10631, 2815, 2702, 2717,2367]
    count_108 = [7526,7264,1820,1879,1740,1888]
    plt.xticks(rotation=70)  
    rects1=plt.bar(index,count_106,width=0.2,alpha=.6 ,  label = '106',)
    rects2=plt.bar(index+0.2,count_107 ,width=0.2,alpha=.6, label = '107 ' )
    rects3=plt.bar(index+0.4,count_108 ,width=0.2,alpha=.6, label = '108 ' )

    def add_labels(rects):#顯示每個長條圖上顯示資料標籤
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
            rect.set_edgecolor('white')

    add_labels(rects1)
    add_labels(rects2)
    add_labels(rects3)
    plt.legend() #要使用label要加這行
    plt.title("近三年肇事因素比較",fontsize=20)
    plt.ylabel("肇事數量",fontsize=15)
    plt.legend(prop = {'size':15})
    plt.grid(True) 
    plt.show() 

def main():
    while True:
        choise = ''
        print ('******************************************')
        print ('               1:路面狀況                  ')
        print ('               2:路面缺陷                  ')
        print ('          3:路面狀況的種類圖表              ')
        print ('          4:路面缺陷的種類圖表              ')
        print ('         5:因路面缺陷導致事故統計圖          ')
        print ('       6: 道路缺陷有無安全標示統計圖         ')
        print ('           7:肇事因素主要五大(BAR)           ')
        print ('        8:肇事因素主要比例(圓餅圖)           ')
        print ('        9:肇事因素主要近三年內比較           ')
        print ('                10:離開                    ')
        print ('******************************************')
    
        choise = input ('請選擇要看的狀況')
        if choise == '1':
            load_situation()
        elif choise == '2':
            load_gap()
        elif choise == '10':
            break
        elif choise == '3':
            load_situation_plt()
        elif choise == '4':
            load_gap_plt()
        elif choise == '5':
            gap_percent()
        elif choise == '6':
            nonotice()
        elif choise == '7':
            accident_fact_five()
        elif choise == '8':
            accident_fact_pie()
        elif choise == '9':
            accident_fact_compare()
        else:
            print('Error,please choise another options')
#main()