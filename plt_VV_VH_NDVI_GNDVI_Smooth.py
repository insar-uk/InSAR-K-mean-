# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取GNDVI和NDVI数据
# # gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\winter_wheat_GNDVI_NDVI_2023.csv'
# # gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)
#
# # 读取VH数据
# vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_amplitude_all.xlsx'
# vh_data = pd.read_excel(vh_file_path)
#
# # 读取VV数据
# vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_amplitude_all.xlsx'
# vv_data = pd.read_excel(vv_file_path)
#
# # 转换日期格式
# # gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
# vh_data['date'] = pd.to_datetime(vh_data['date'])
# vv_data['date'] = pd.to_datetime(vv_data['date'])
#
# # 按日期排序
# # gndvi_ndvi_data.sort_values('Date', inplace=True)
# vh_data.sort_values('date', inplace=True)
# vv_data.sort_values('date', inplace=True)
#
# # 创建绘图
# plt.figure(figsize=(12, 9))
# plt.subplots_adjust(bottom=0.15)
#
# # 指数平滑窗口大小
# span = 3# 你可以根据需要调整这个参数
#
# # 绘制GNDVI
# # gndvi_ndvi_data['GNDVI_Mean_Smoothed'] = gndvi_ndvi_data['GNDVI_Mean'].ewm(span=span, adjust=False).mean()
# # plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean'], color='green', label='GNDVI Mean')
# # plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['GNDVI_Mean_Smoothed'], color='green')
# #
# # # 绘制NDVI
# # gndvi_ndvi_data['NDVI_Mean_Smoothed'] = gndvi_ndvi_data['NDVI_Mean'].ewm(span=span, adjust=False).mean()
# # plt.scatter(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean'], color='blue', label='NDVI Mean')
# # plt.plot(gndvi_ndvi_data['Date'], gndvi_ndvi_data['NDVI_Mean_Smoothed'], color='blue')
#
# # 绘制VH
# vh_data['mean_Smoothed'] = vh_data['mean'].ewm(span=span, adjust=False).mean()
# # plt.scatter(vh_data['date'], vh_data['mean'], color='red', label='VH Amplitude Mean')
# plt.plot(vh_data['date'], vh_data['mean_Smoothed'], color='red', label='VH Amplitude Smooth')
#
# # 绘制VV
# vv_data['mean_Smoothed'] = vv_data['mean'].ewm(span=span, adjust=False).mean()
# # plt.scatter(vv_data['date'], vv_data['mean'], color='purple', label='VV Amplitude Mean')
# plt.plot(vv_data['date'], vv_data['mean_Smoothed'], color='purple', label='VV Amplitude Smooth')
#
# # 设置x轴刻度为月份
# plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))
# date_ticks = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')  # MS: month start
# date_labels = [date.strftime('%Y-%m') for date in date_ticks]
# plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
#
# # 设置标题和标签
# plt.yticks(fontsize=14)
# plt.title('VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
# plt.xlabel('Date', fontsize=16)
# plt.ylabel('Index Value', fontsize=16)
#
# # 图例
# plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0))
#
# # 设置Y轴范围
# plt.ylim(2.5, 4.5)
#
# # 移除格网
# plt.grid(False)
#
# # 保存并显示图表
# output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_amplitude_daily_over_time_smooth.jpg'
# plt.savefig(output_file_path, format='jpg')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9), dpi=300)
plt.subplots_adjust(bottom=0.15)

# 移动平均窗口大小
window_size = 5# 你可以根据需要调整这个参数

# 绘制VH
vh_data['mean_Smoothed'] = vh_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vh_data['date'], vh_data['mean'], color='red', label='VH Amplitude Mean')
plt.plot(vh_data['date'], vh_data['mean_Smoothed'], color='red', label='VH Amplitude Smooth')

# 绘制VV
vv_data['mean_Smoothed'] = vv_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vv_data['date'], vv_data['mean'], color='purple', label='VV Amplitude Mean')
plt.plot(vv_data['date'], vv_data['mean_Smoothed'], color='purple', label='VV Amplitude Smooth')

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

# 图例
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0))

# 设置Y轴范围
plt.ylim(2.5, 4.5)

# 移除格网
plt.grid(False)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_amplitude_daily_over_time_smooth_mean.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_Coherence_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_Coherence_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9), dpi=300)
plt.subplots_adjust(bottom=0.15)

# 移动平均窗口大小
window_size = 5# 你可以根据需要调整这个参数

# 绘制VH
vh_data['mean_Smoothed'] = vh_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vh_data['date'], vh_data['mean'], color='red', label='VH Amplitude Mean')
plt.plot(vh_data['date'], vh_data['mean_Smoothed'], color='red', label='VH Coherence Smooth')

# 绘制VV
vv_data['mean_Smoothed'] = vv_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vv_data['date'], vv_data['mean'], color='purple', label='VV Amplitude Mean')
plt.plot(vv_data['date'], vv_data['mean_Smoothed'], color='purple', label='VV Coherence Smooth')

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

# 图例
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0))

# 设置Y轴范围
plt.ylim(0, 1)

# 移除格网
plt.grid(False)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_coherence_daily_over_time_smooth_mean.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9), dpi=300)
plt.subplots_adjust(bottom=0.15)

# 移动平均窗口大小
window_size = 5# 你可以根据需要调整这个参数

# 绘制VH
vh_data['mean_Smoothed'] = vh_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vh_data['date'], vh_data['mean'], color='red', label='VH Amplitude Mean')
plt.plot(vh_data['date'], vh_data['mean_Smoothed'], color='red', label='VH Amplitude Smooth')

# 绘制VV
vv_data['mean_Smoothed'] = vv_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vv_data['date'], vv_data['mean'], color='purple', label='VV Amplitude Mean')
plt.plot(vv_data['date'], vv_data['mean_Smoothed'], color='purple', label='VV Amplitude Smooth')

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

# 图例
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0))

# 设置Y轴范围
plt.ylim(2.5, 4.5)

# 移除格网
plt.grid(False)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\Barley_amplitude_daily_over_time_smooth_mean.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# 读取VH数据
vh_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VH_Coherence_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# 读取VV数据
vv_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VV_Coherence_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# 转换日期格式
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# 按日期排序
vh_data.sort_values('date', inplace=True)
vv_data.sort_values('date', inplace=True)

# 创建绘图
plt.figure(figsize=(12, 9), dpi=300)
plt.subplots_adjust(bottom=0.15)

# 移动平均窗口大小
window_size = 5# 你可以根据需要调整这个参数

# 绘制VH
vh_data['mean_Smoothed'] = vh_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vh_data['date'], vh_data['mean'], color='red', label='VH Amplitude Mean')
plt.plot(vh_data['date'], vh_data['mean_Smoothed'], color='red', label='VH Coherence Smooth')

# 绘制VV
vv_data['mean_Smoothed'] = vv_data['mean'].rolling(window=window_size, center=True).mean()
# plt.scatter(vv_data['date'], vv_data['mean'], color='purple', label='VV Amplitude Mean')
plt.plot(vv_data['date'], vv_data['mean_Smoothed'], color='purple', label='VV Coherence Smooth')

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

# 图例
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0))

# 设置Y轴范围
plt.ylim(0, 1)

# 移除格网
plt.grid(False)

# 保存并显示图表
output_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\Barley_coherence_daily_over_time_smooth_mean.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()