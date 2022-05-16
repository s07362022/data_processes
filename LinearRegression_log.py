from numpy.core.defchararray import index
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('trace.csv')
df1=df.drop( df.columns[0],axis=1)
inx=df1[df1.x == 0].index
df1= df1.drop(inx)
df1.reset_index(inplace=True,drop=True)
t =(df1.iloc[21])
df1= df1.drop(21)
df1.reset_index(inplace=True,drop=True)
#print(df1)
#print(t[0])
# show scatter
'''
plt.scatter(df1.x,df1.y,color = 'darkgreen',label = "Exam Data")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
'''


q = df1.corr()#查看數據間的相關係數
#print(q)
X_train,X_test,Y_train,Y_test = train_test_split(df1.x,df1.y,train_size=0.8)
#show scatter
#plt.scatter(X_train, Y_train, color="darkgreen", label="train data")#訓練集爲深綠色點
#plt.scatter(X_test, Y_test, color="red", label="test data")#測試集爲紅色點
#plt.show()

#線性迴歸訓練
model = LinearRegression(fit_intercept=True)
model.fit(X_train.values.reshape(-1, 1),Y_train.values.reshape(-1, 1))#調用線性迴歸包

a  = model.intercept_#截距
a = np.round(a[0],2)
b = model.coef_#迴歸係數
b = np.round(b[0][0],2)
y_train_pred = model.predict(X_train.values.reshape(-1, 1))
y_train_pred=y_train_pred.reshape(-1,)
plt.plot(X_train, y_train_pred, color='blue', linewidth=2, label="best line")
#測試數據散點圖
plt.scatter(X_train, Y_train, color='darkgreen', label="train data")
plt.scatter(X_test, Y_test, color='red', label="test data")
print("擬合參數:截距",a,",迴歸係數：",b)
print("最佳擬合線: Y = ",a,"+",b,"* X")
#plt.show()
re =  a + b* t[0]
print("test_x",t[0],"test_y",t[1])
print("predict_y",re)

plt.scatter( t[0], re, color='black', label="re")
plt.show()
