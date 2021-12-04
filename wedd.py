import pandas as pd
df = pd.read_csv("train.csv")
df.dropna(
    axis=0,     
    how='any',   
    inplace=True)
## 檢查是否還有缺失值
df.isnull().sum(axis=0)
#reset index
df = df.reset_index(drop=True)
df2 = pd.get_dummies(df)
df2.head()
df2['contp'].value_counts()
df['stscd'].value_counts()
df['flbmk'].value_counts()
data = df2.drop('fraud_ind',axis=1)
label = df2['fraud_ind']
### 請架設模型並訓練
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
#做資料切行，且幫你做洗牌，因為考慮到data的排列具有某種邏輯存在
X_train,X_test,y_train,y_test = train_test_split(data,label,test_size=0.3,random_state=2)
X_train.shape,X_test.shape

mode1 = DecisionTreeClassifier(max_depth=5)
mode2 = KNeighborsClassifier(n_neighbors=2)
mode3 = SVC(kernel='rbf',probability=True)

eclf = VotingClassifier(estimators=[('dt', mode1), ('knn', mode2),('svc', mode3)], voting='soft', weights=[2,1,1])
eclf.fit(X_train, y_train)
print(metrics.classification_report(y_test, eclf.predict(X_test)))