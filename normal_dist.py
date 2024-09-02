import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from scipy.stats import norm

# 示例的 xy 座標數據
x = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 擬合 x 和 y 的正態分佈
mu_x, std_x = norm.fit(x)
mu_y, std_y = norm.fit(y)

# 生成 x 軸數據和正態分佈曲線
x_vals = np.linspace(min(x), max(x), 100)
y_vals = np.linspace(min(y), max(y), 100)
pdf_x = norm.pdf(x_vals, mu_x, std_x)
pdf_y = norm.pdf(y_vals, mu_y, std_y)

# 計算每個點與正態分佈均值的距離
distances = np.sqrt((x - mu_x)**2 + (y - mu_y)**2)

# 找到距離最大的點 (極端點)
extreme_index = np.argmax(distances)
extreme_point = (x[extreme_index], y[extreme_index])

# 創建一個圖表
fig = make_subplots(rows=1, cols=1)

# 添加原始數據點
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data Points', marker=dict(color='red')))

# 添加正態分佈曲線
fig.add_trace(go.Scatter(x=x_vals, y=pdf_x * max(y) * 10, mode='lines', name='Normal Distribution X'))
fig.add_trace(go.Scatter(x=y_vals, y=pdf_y * max(x) * 10, mode='lines', name='Normal Distribution Y'))

# 標註極端點
fig.add_trace(go.Scatter(x=[extreme_point[0]], y=[extreme_point[1]], mode='markers+text',
                         name='Extreme Point', text='Extreme', textposition='top center',
                         marker=dict(color='blue', size=10)))

# 設置圖表標題和軸標籤
fig.update_layout(title='Normal Distribution with Data Points and Extreme Point',
                  xaxis_title='X',
                  yaxis_title='Y')

# 顯示圖表
fig.show()

print(f"極端點是: {extreme_point}")