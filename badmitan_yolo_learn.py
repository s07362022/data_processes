import cv2
import time

CONFIDENCE_THRESHOLD = 0.7
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
#D:\\yolov4\\darknet-master\\darknet-master\\build\\darknet\\x64\\coco.names
class_names = []
with open("obj.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

vc = cv2.VideoCapture("ball17.mp4")#("ball17.mp4")
#"D:\\yolov4\\darknet-master\\darknet-master\\build\\darknet\\x64\\yolov3.weights", "D:\\yolov4\\darknet-master\\darknet-master\\build\\darknet\\x64\\cfg\\yolov3.cfg"
net = cv2.dnn.readNet("yolov3_bad.cfg","yolov3_bad_best.weights")
#net = cv2.dnn.readNet("yolov3_bad.cfg","yolov3_bad_best.weights")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

#####################location algo ################
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
model_line = LinearRegression(fit_intercept=True)
x_list = []
y_list = []
all_list = [x_list,y_list]
#all_list=np.transpose(all_list)
prev_list_x=[]
prev_list_y =[]
print(type(all_list[0]))
###################################################
while cv2.waitKey(1) < 1:
    (grabbed, frame) = vc.read()
    if not grabbed:
        exit()

    start = time.time()
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    end = time.time()

    start_drawing = time.time()
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        ####algo#####
        #print(box)
        if (box[0]>970 or box[0]<930)and (box[1]>=290) :
            all_list[0].append(box[0])
            all_list[1].append(box[1])
        try:
            if y_list[-2]>=290 and y_list[-1]>=290:
                #all_list = [x_list,y_list]
                df = pd.DataFrame(all_list)
                df=df.T
                df.columns=["x","y"]
                df1 = df.copy()
                inx=df1[df1.x == 0].index
                df1= df1.drop(inx)
                df1.reset_index(inplace=True,drop=True)
                df2=df1.tail(5)
                t=df2.x.values[-1]
                model_line.fit(df2.x.values.reshape(-1,1),df2.y.values.reshape(-1,1))
                a  = model_line.intercept_#截距
                a = np.round(a[0],2)
                b = model_line.coef_#迴歸係數
                b = np.round(b[0][0],2)
                print("最佳擬合線: Y = ",a,"+",b,"* X")
                re =  a + b* (t)
                t = int((re+40-a)/b)
                re =  a + b* (t)
                #re =  a + b* (t+re)
                re = int(re)
                print("x:",t,"predict_y:",re)
                prev_list_x.append(t)
                prev_list_y.append(re)
                
                #cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        except:
            pass
        ############
        
    end_drawing = time.time()
    
    fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    try:
        text_="prediction x:"+str(t)+"prediction y:"+str(re)
        cv2.circle(frame, (prev_list_x[-1], prev_list_y[-1]), 10, (0,0,255), cv2.FILLED)
        cv2.putText(frame,text_ , (100,  100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    except:
        pass
    cv2.imshow("detections", frame)
