import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from matplotlib.pyplot import MultipleLocator
from scipy.signal import find_peaks
from scipy.signal import butter, lfilter, filtfilt, savgol_filter
from scipy.signal import find_peaks
#Python之pandas读取Excel表格空值为nan的处理 https://blog.csdn.net/wl_Honest/article/details/99082977
#第一步選定需要比較的檔案
def coma(df):
    
    listRX1=[]
    listRX2=[]

    listRY1=[]
    listRY2=[]

    listRZ1=[]
    listRZ2=[]

    listLX1=[]
    listLX2=[]

    listLY1=[]
    listLY2=[]

    listLZ1=[]
    listLZ2=[]


    listGRX=[]
    listGRY=[]
    listGRZ=[]

    listGLX=[]
    listGLY=[]
    listGLZ=[]


    listflag_Record=[]
    listflag_one=[]
    listflag_two=[]
    listflag_three=[]

    listRtoe=[]
    listLtoe=[]

    listRX1=df.RightFootAcc_X.tolist() 
    listRY1=df.RightFootAcc_Y.tolist() 
    listRZ1=df.RightFootAcc_Z.tolist() 

    listLX1=df.LeftFootAcc_X.tolist() 
    listLY1=df.LeftFootAcc_Y.tolist() 
    listLZ1=df.LeftFootAcc_Z.tolist() 


    listGRX=df.RightFootGyro_X.tolist()
    listGRY=df.RightFootGyro_Y.tolist()
    listGRZ=df.RightFootGyro_Z.tolist()

    listGLX=df.LeftFootGyro_X.tolist()
    listGLY=df.LeftFootGyro_Y.tolist()
    listGLZ=df.LeftFootGyro_Z.tolist()

    listflag_Record=df.Record.tolist()
    listflag_one=df.Record.tolist()
    listflag_two=df.Record.tolist()
    listflag_three=df.Record.tolist()


    #去除空白
    listRX1 = [i for i in listRX1 if i != '']
    listRX2 = [i for i in listRX2 if i != '']

    listRY1 = [i for i in listRY1 if i != '']
    listRY2 = [i for i in listRY2 if i != '']

    listRZ1 = [i for i in listRZ1 if i != '']
    listRZ2 = [i for i in listRZ2 if i != '']

    listLX1 = [i for i in listLX1 if i != '']
    listLX2 = [i for i in listLX2 if i != '']

    listLY1 = [i for i in listLY1 if i != '']
    listLY2 = [i for i in listLY2 if i != '']

    listLZ1 = [i for i in listLZ1 if i != '']
    listLZ2 = [i for i in listLZ2 if i != '']

    listGRX = [i for i in listGRX if i != '']
    listGRY = [i for i in listGRY if i != '']
    listGRZ = [i for i in listGRZ if i != '']

    listGLX = [i for i in listGLX if i != '']
    listGLY = [i for i in listGLY if i != '']
    listGLZ = [i for i in listGLZ if i != '']



   

    #抓出雙腳最大承認點數
    gaitmin=0
    if(len(listRX1)<len(listLX1)):
        gaitmin=len(listRX1)
    else:
        gaitmin=len(listLX1)
    print(gaitmin)
    #gaitmin=
    # #抓二級二級疼痛
    # for f in range(a):
    #     if(listflag_Record[f]=='2級二級疼痛'):
    #         listflag_Record[f]=f
    #     else:
    #         listflag_Record[f]=''
    # listflag_Record = [i for i in listflag_Record if i != '']

    #抓轉彎
    for f in range(len(listflag_Record)):
         if (f >= gaitmin):
            listflag_Record[f]=''
        
         elif(listflag_Record[f]=='轉彎'):
            listflag_Record[f]=f
        
         else:
            listflag_Record[f]=''

    listflag_Record = [i for i in listflag_Record if i != '']

    #抓一級二級疼痛
    for f in range(len(listflag_one)):
        
        if (f >= gaitmin):
            listflag_one[f]=''
        
        elif(listflag_one[f]=='1級疼痛'):
            listflag_one[f]=f
        
        else:
            listflag_one[f]=''

    listflag_one = [i for i in listflag_one if i != '']
    


    #抓二級二級疼痛
    for f in range(len(listflag_two)):
        if (f >= gaitmin):
            listflag_two[f]=''
        
        elif(listflag_two[f]=='2級疼痛'):
            listflag_two[f]=f
        
        else:
            listflag_two[f]=''
    listflag_two = [i for i in listflag_two if i != '']


    #抓三級二級疼痛
    for f in range(len(listflag_three)):
        if (f >= gaitmin):
            listflag_three[f]=''
        
        elif(listflag_three[f]=='3級疼痛'):
            listflag_three[f]=f
        
        else:
            listflag_three[f]=''
    listflag_three = [i for i in listflag_three if i != '']


    l=len(listRX1)
    #右腳X要乘-1
    for i in range(l):
        listRX1[i]= listRX1[i]*(-1)

    l=len(listGRZ)
    #右腳陀螺儀Z軸要乘-1
    for i in range(l):
        listGRZ[i]= listGRZ[i]*(-1)

    listRrss=[]
    for i in range(len(listRX1)): 
        listRrss.append(np.sqrt((listRX1[i] ** 2) + (listRY1[i] ** 2) + (listRZ1[i] ** 2))) 

    listLrss=[]
    for i in range(len(listLX1)): 
        listLrss.append(np.sqrt((listLX1[i] ** 2) + (listLY1[i] ** 2) + (listLZ1[i] ** 2))) 
    

    return listRX1,listRY1,listRZ1,listLX1,listLY1,listLZ1,listflag_Record,listflag_one,listflag_two,listflag_three,listGRX,listGRY,listGRZ,listGLX,listGLY,listGLZ,listRrss,listLrss





#第一步選定需要比較的檔案
df = pd.read_excel("李O貴2.xlsx",keep_default_na=False)
listRX1,listRY1,listRZ1,listLX1,listLY1,listLZ1,listflag_Record,listflag_one,listflag_two,listflag_three,listGRX,listGRY,listGRZ,listGLX,listGLY,listGLZ,listRrss,listLrss=coma(df)

# df = pd.read_excel("轉彎.xlsx",keep_default_na=False)
# listRX1,listRY1,listRZ1,listLX1,listLY1,listLZ1,listflag_Record=coma(df)


# #
# #第二步選定切割的檔案"
# df = pd.read_excel("總李O貴2(手動切割).xlsx",keep_default_na=False)

# one=[]
# two=[]
# three=[]
# four=[]

# #one[0]為右腳第一步起始點
# one=df.Rtoe_off.tolist()


# #two[0]為左腳第一步起始點
# two=df.Ltoe_off.tolist() 


# #three為右腳每步間距點
# for i in range(len(one)-1):
#     three.append(one[i+1]-one[i])


# #four為左腳每步間距點
# for i in range(len(two)-1):
#     four.append(two[i+1]-two[i])



# print("右腳總步數")
# print(len(three)+1)
# #右腳:可以讓(後減前)=剩餘位置
# print("右腳每步間距")
# print(three)
# print("=====================================================================================================================================")

# print("左腳總步數")
# print(len(four)+1)
# #左腳:可以讓(後減前)=剩餘位置 
# print("左腳每步間距")
# print(four)
# print("=====================================================================================================================================")


if(len(listflag_Record)%2!=0):
    print("請先手動輸入補差值")
    print("=====================================================================================================================================")
    print("轉彎位置")
    print(listflag_Record)

# print(listflag_one)
# print(listflag_two)
# print(listflag_three)
#listGRY= savgol_filter(listGRY,30,3)
listGRX= savgol_filter(listGRX,20,3)
listGRY= savgol_filter(listGRY,30,3)
listGRZ= savgol_filter(listGRZ,30,3)



def G_plot(Gname,G,flagturn,flagone,flagtwo):#

    R_pain=np.array(G[000:18499])
    R_pain_peaks, _= find_peaks(R_pain,height=50,distance=70)
    plt.title(str(Gname))
    
    for i in range(len(flagturn)):
        plt.axvline(x=flagturn[i],color='orange',label='轉彎')
      

    for i in range(len(flagone)):
        plt.axvline(x=flagone[i],color='red',label='一級疼痛')
     

    for i in range(len(flagtwo)):
        plt.axvline(x=flagtwo[i],color='blue',label='二級疼痛')

    labels = ['轉彎','一級疼痛','二級疼痛']
    plt.legend(labels)
    plt.plot(R_pain)
    plt.plot(R_pain_peaks, R_pain[R_pain_peaks],"*")
    plt.show()




G_plot("listGRX",listGRX,listflag_Record,listflag_one,listflag_two)
#G_plot("listGRY",listGRY,listflag_Record,listflag_one,listflag_two)
#G_plot("listGRZ",listGRZ,listflag_Record,listflag_one,listflag_two)
