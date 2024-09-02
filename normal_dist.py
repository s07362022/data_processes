import numpy as np
import plotly.graph_objs as go
from scipy.stats import multivariate_normal

# 示例的 xy 座標數據 (增加數據點以更好地展示分佈)
xy = np.array([[10, 1], [12, 2], [14, 3], [16, 4], [18, 5],
               [20, 6], [22, 7], [24, 8], [26, 9], [28, 10],
               [15, 3], [13, 4], [17, 6], [19, 7], [21, 5],
               [23, 8], [25, 9], [27, 10], [29, 11], [30, 12]])

# 計算 xy 的均值和協方差矩陣
mu = np.mean(xy, axis=0)
cov = np.cov(xy, rowvar=False)

# 創建二維正態分佈
rv = multivariate_normal(mu, cov)

# 生成網格數據以計算PDF
x_vals = np.linspace(min(xy[:, 0]) - 5, max(xy[:, 0]) + 5, 100)
y_vals = np.linspace(min(xy[:, 1]) - 5, max(xy[:, 1]) + 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
pos = np.dstack((X, Y))
Z = rv.pdf(pos)

# 繪製數據點和正態分佈等高線
fig = go.Figure()

# 添加數據點
fig.add_trace(go.Scatter(x=xy[:, 0], y=xy[:, 1], mode='markers', name='Data Points', marker=dict(color='red')))

# 添加等高線
fig.add_trace(go.Contour(x=x_vals, y=y_vals, z=Z, colorscale='Viridis', name='Normal Distribution'))

# 找到距離最大的點 (極端點)
distances = np.linalg.norm(xy - mu, axis=1)
extreme_index = np.argmax(distances)
extreme_point = xy[extreme_index]

# 標註極端點
fig.add_trace(go.Scatter(x=[extreme_point[0]], y=[extreme_point[1]], mode='markers+text',
                         name='Extreme Point', text='Extreme', textposition='top center',
                         marker=dict(color='blue', size=10)))

# 設置圖表標題和軸標籤
fig.update_layout(title='2D Normal Distribution with Data Points and Extreme Point',
                  xaxis_title='X',
                  yaxis_title='Y')

# 顯示圖表
fig.show()

print(f"極端點是: {extreme_point}")