import numpy as np
import plotly.graph_objs as go

# 示例的 xy 座標數據
xy = np.array([[10, 1], [12, 2], [14, 3], [16, 4], [18, 5],
               [20, 6], [22, 7], [24, 8], [26, 9], [28, 10]])

# 計算 xy 的均值
mu = np.mean(xy, axis=0)

# 找到距離最大的點 (極端點)
distances = np.linalg.norm(xy - mu, axis=1)
extreme_index = np.argmax(distances)
extreme_point = xy[extreme_index]

# 繪製數據點
fig = go.Figure()

# 添加數據點
fig.add_trace(go.Scatter(x=xy[:, 0], y=xy[:, 1], mode='markers', name='Data Points', marker=dict(color='red')))

# 標註極端點
fig.add_trace(go.Scatter(x=[extreme_point[0]], y=[extreme_point[1]], mode='markers+text',
                         name='Extreme Point', text='Extreme', textposition='top center',
                         marker=dict(color='blue', size=10)))

# 設置圖表標題和軸標籤
fig.update_layout(title='Scatter Plot with Extreme Point',
                  xaxis_title='X',
                  yaxis_title='Y')

# 顯示圖表
fig.show()

print(f"極端點是: {extreme_point}")