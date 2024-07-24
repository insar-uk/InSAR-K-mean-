

import pandas as pd
import matplotlib.pyplot as plt

# 读取GNDVI和NDVI数据
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\winter_wheat_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
gndvi_ndvi_data.sort_values('Date', inplace=True)
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
# 绘制GNDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], label='GNDVI Mean', color='green')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], color='green')

# 绘制NDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], label='NDVI Mean', color='blue')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], color='blue')

# 绘制VH
plt.plot(vh_data['date'], vh_data['mean'], label='VH Amplitude Mean', color='red')
plt.scatter(vh_data['date'], vh_data['mean'], color='red')

# 绘制VV
plt.plot(vv_data['date'], vv_data['mean'], label='VV Amplitude Mean', color='purple')
plt.scatter(vv_data['date'], vv_data['mean'], color='purple')

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('NDVI, GNDVI, VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.2))
# 显示图例
# plt.legend()
# 设置Y轴范围
plt.ylim(0, 5)

# 移除格网
plt.grid(False)
# 显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_amplitude_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()
#





import pandas as pd
import matplotlib.pyplot as plt

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

# 创建绘图
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
# 绘制GNDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], label='GNDVI Mean', color='green')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], color='green')

# 绘制NDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], label='NDVI Mean', color='blue')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], color='blue')

# 绘制VH
plt.plot(vh_data['date'], vh_data['mean'], label='VH Coherence Mean', color='red')
plt.scatter(vh_data['date'], vh_data['mean'], color='red')

# 绘制VV
plt.plot(vv_data['date'], vv_data['mean'], label='VV Coherence Mean', color='purple')
plt.scatter(vv_data['date'], vv_data['mean'], color='purple')

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('NDVI, GNDVI, VH, and VV Coherence Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))
# 显示图例
# plt.legend()
# 设置Y轴范围
plt.ylim(0, 1)

# 移除格网
plt.grid(False)
# 显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_coherence_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# 读取GNDVI和NDVI数据
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\winter_Barley_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
gndvi_ndvi_data.sort_values('Date', inplace=True)
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
# 绘制GNDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], label='GNDVI Mean', color='green')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], color='green')

# 绘制NDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], label='NDVI Mean', color='blue')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], color='blue')

# 绘制VH
plt.plot(vh_data['date'], vh_data['mean'], label='VH Amplitude Mean', color='red')
plt.scatter(vh_data['date'], vh_data['mean'], color='red')

# 绘制VV
plt.plot(vv_data['date'], vv_data['mean'], label='VV Amplitude Mean', color='purple')
plt.scatter(vv_data['date'], vv_data['mean'], color='purple')

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('NDVI, GNDVI, VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.2))
# 显示图例
# plt.legend()
# 设置Y轴范围
plt.ylim(0, 5)

# 移除格网
plt.grid(False)
# 显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\Barley_amplitude_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# 读取GNDVI和NDVI数据
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\winter_Barley_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VH_Coherence_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VV_Coherence_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
gndvi_ndvi_data.sort_values('Date', inplace=True)
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
# 绘制GNDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], label='GNDVI Mean', color='green')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], color='green')

# 绘制NDVI
plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], label='NDVI Mean', color='blue')
plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], color='blue')

# 绘制VH
plt.plot(vh_data['date'], vh_data['mean'], label='VH Coherence Mean', color='red')
plt.scatter(vh_data['date'], vh_data['mean'], color='red')

# 绘制VV
plt.plot(vv_data['date'], vv_data['mean'], label='VV Coherence Mean', color='purple')
plt.scatter(vv_data['date'], vv_data['mean'], color='purple')

# 设置x轴刻度为月份
plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
# 设置标题和标签
plt.yticks(fontsize=14)
plt.title('NDVI, GNDVI, VH, and VV Coherence Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))
# 显示图例
# plt.legend()
# 设置Y轴范围
plt.ylim(0,1)

# 移除格网
plt.grid(False)
# 显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\Barley_coherence_daily_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()