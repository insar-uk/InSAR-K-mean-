import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 读取GNDVI和NDVI数据
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\winter_wheat_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_Coherence_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_Coherence_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
gndvi_ndvi_data.sort_values('Date', inplace=True)
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)
print(vv_data)
# 创建绘图
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)

# 绘制GNDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], label='GNDVI Mean', color='green', linewidth=0.8)

# 绘制NDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], label='NDVI Mean', color='blue', linewidth=0.8)

# K-means聚类
kmeans_gndvi = KMeans(n_clusters=4, random_state=2).fit(gndvi_ndvi_data[['GNDVI_Mean']])
kmeans_ndvi = KMeans(n_clusters=4, random_state=2).fit(gndvi_ndvi_data[['NDVI_Mean']])

# 添加聚类结果的散点图
scatter_gndvi = plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], c=kmeans_gndvi.labels_, cmap='viridis', marker='o', s=16)
scatter_ndvi = plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], c=kmeans_ndvi.labels_, cmap='viridis', marker='o', s=16)

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)

# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('NDVI and GNDVI Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))

# 设置Y轴范围
plt.ylim(0, 1)

# 移除格网
plt.grid(False)

# 添加颜色条
cbar = plt.colorbar(scatter_ndvi)
cbar.set_label('Cluster', fontsize=16)
cbar.ax.tick_params(labelsize=14)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\kmeans_wheat_NDVI_GNDVI_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()



plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)

plt.plot(vh_data['date'], vh_data['mean'],
         label='VH Coherence Mean', color='green', marker=None, linewidth=0.8)

# Plot VV mean as a line plot
plt.plot(vv_data['date'], vv_data['mean'],
         label='VH Coherence Mean', color='blue', marker=None, linewidth=0.8)
# Define cluster colors


# K-means聚类
kmeans_vh = KMeans(n_clusters=4, random_state=2).fit(vh_data[['mean', 'std']])
kmeans_vv = KMeans(n_clusters=4, random_state=2).fit(vv_data[['mean', 'std']])

# 添加聚类结果的散点图
scatter_vh = plt.scatter(vh_data['date'], vh_data['mean'], c=kmeans_vh.labels_, cmap='viridis', marker='o', s=16)
scatter_vv = plt.scatter(vv_data['date'], vv_data['mean'], c=kmeans_vv.labels_, cmap='viridis', marker='o', s=16)

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)

# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('VH, and VV Coherence Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))

# 设置Y轴范围
plt.ylim(0, 1)

# 移除格网
plt.grid(False)

# 添加颜色条
cbar = plt.colorbar(scatter_vv)
cbar.set_label('Cluster', fontsize=16)
cbar.ax.tick_params(labelsize=14)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\kmeans_wheat_VV_VH_Coherence_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()






# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)


vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)




plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)

plt.plot(vh_data['date'], vh_data['mean'],
         label='VH Amplitude Mean', color='green', marker=None, linewidth=0.8)

# Plot VV mean as a line plot
plt.plot(vv_data['date'], vv_data['mean'],
         label='VV Amplitude Mean', color='blue', marker=None, linewidth=0.8)
# Define cluster colors


# K-means聚类
kmeans_vh = KMeans(n_clusters=4, random_state=2).fit(vh_data[['mean', 'std']])
kmeans_vv = KMeans(n_clusters=4, random_state=2).fit(vv_data[['mean', 'std']])

# 添加聚类结果的散点图
scatter_vh = plt.scatter(vh_data['date'], vh_data['mean'], c=kmeans_vh.labels_, cmap='viridis', marker='o', s=16)
scatter_vv = plt.scatter(vv_data['date'], vv_data['mean'], c=kmeans_vv.labels_, cmap='viridis', marker='o', s=16)

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)

# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))

# 设置Y轴范围
plt.ylim(2, 5)

# 移除格网
plt.grid(False)

# 添加颜色条
cbar = plt.colorbar(scatter_vv)
cbar.set_label('Cluster', fontsize=16)
cbar.ax.tick_params(labelsize=14)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\kmeans_wheat_VV_VH_Amplitude_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()







