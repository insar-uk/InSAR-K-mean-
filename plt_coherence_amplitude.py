import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# 读取Excel文件
amplitude_file = r'D:\BaiduNetdiskDownload\2023\Winter_Barley_result_all\VV_amplitude_all_monthly.xlsx'
coherence_file = r'D:\BaiduNetdiskDownload\2023\Winter_Barley_result_all\VV_Coherence_all_monthly.xlsx'

amplitude_df = pd.read_excel(amplitude_file)
coherence_df = pd.read_excel(coherence_file)

# 重命名列以便合并
amplitude_df.rename(columns={'mean_value': 'amplitude_mean', 'std_dev_mean': 'amplitude_std_dev'}, inplace=True)
coherence_df.rename(columns={'mean_value': 'coherence_mean', 'std_dev_mean': 'coherence_std_dev'}, inplace=True)

# 根据 year_month 进行合并
df = pd.merge(amplitude_df, coherence_df, on='year_month')

# 选择需要的数据
data = df[['coherence_mean', 'amplitude_mean']]

# 应用 KMeans 聚类
kmeans = KMeans(n_clusters=4, random_state=2).fit(data)
df['cluster'] = kmeans.labels_
df['date'] = pd.to_datetime(df['year_month'])

# 绘制散点图
plt.figure(figsize=(20, 16))
scatter = plt.scatter(df['coherence_mean'], df['amplitude_mean'], c=df['cluster'], cmap='viridis', marker='o')

# 在散点上标注日期
for i, row in df.iterrows():
    plt.annotate(f"{row['date'].strftime('%m')}",
                 (row['coherence_mean'], row['amplitude_mean']),
                 textcoords="offset points",
                 xytext=(0, 3),
                 ha='center',
                 fontsize=18)

plt.xlabel('VV Coherence Mean', fontsize=20)
plt.ylabel('VV Amplitude Mean', fontsize=20)
plt.title('KMeans Clustering of Barley VV Coherence and Amplitude', fontsize=18)
cbar = plt.colorbar(scatter, label='Cluster')
cbar.ax.tick_params(labelsize=18)
cbar.set_label('Cluster', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)
output_file = os.path.join(r'D:\BaiduNetdiskDownload\2023\coherence_amplitude', 'Barley_VV_coherence_amplitude_kmeans_scatter.png')
plt.savefig(output_file)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# 读取Excel文件
amplitude_file = r'D:\BaiduNetdiskDownload\2023\Winter_Barley_result_all\VH_amplitude_all_monthly.xlsx'
coherence_file = r'D:\BaiduNetdiskDownload\2023\Winter_Barley_result_all\VH_Coherence_all_monthly.xlsx'

amplitude_df = pd.read_excel(amplitude_file)
coherence_df = pd.read_excel(coherence_file)

# 重命名列以便合并
amplitude_df.rename(columns={'mean_value': 'amplitude_mean', 'std_dev_mean': 'amplitude_std_dev'}, inplace=True)
coherence_df.rename(columns={'mean_value': 'coherence_mean', 'std_dev_mean': 'coherence_std_dev'}, inplace=True)

# 根据 year_month 进行合并
df = pd.merge(amplitude_df, coherence_df, on='year_month')

# 选择需要的数据
data = df[['coherence_mean', 'amplitude_mean']]

# 应用 KMeans 聚类
kmeans = KMeans(n_clusters=4, random_state=2).fit(data)
df['cluster'] = kmeans.labels_
df['date'] = pd.to_datetime(df['year_month'])

# 绘制散点图
plt.figure(figsize=(20, 16))
scatter = plt.scatter(df['coherence_mean'], df['amplitude_mean'], c=df['cluster'], cmap='viridis', marker='o')

# 在散点上标注日期
for i, row in df.iterrows():
    plt.annotate(f"{row['date'].strftime('%m')}",
                 (row['coherence_mean'], row['amplitude_mean']),
                 textcoords="offset points",
                 xytext=(0, 3),
                 ha='center',
                 fontsize=18)

plt.xlabel('VH Coherence Mean', fontsize=20)
plt.ylabel('VH Amplitude Mean', fontsize=20)
plt.title('KMeans Clustering of Barley VH Coherence and Amplitude', fontsize=18)
cbar = plt.colorbar(scatter, label='Cluster')
cbar.ax.tick_params(labelsize=18)
cbar.set_label('Cluster', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)
output_file = os.path.join(r'D:\BaiduNetdiskDownload\2023\coherence_amplitude', 'Barley_VH_coherence_amplitude_kmeans_scatter.png')
plt.savefig(output_file)
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# 读取Excel文件
amplitude_file = r'D:\BaiduNetdiskDownload\2023\Winter_wheat_result_all\VV_amplitude_all_monthly.xlsx'
coherence_file = r'D:\BaiduNetdiskDownload\2023\Winter_wheat_result_all\VV_Coherence_all_monthly.xlsx'

amplitude_df = pd.read_excel(amplitude_file)
coherence_df = pd.read_excel(coherence_file)

# 重命名列以便合并
amplitude_df.rename(columns={'mean_value': 'amplitude_mean', 'std_dev_mean': 'amplitude_std_dev'}, inplace=True)
coherence_df.rename(columns={'mean_value': 'coherence_mean', 'std_dev_mean': 'coherence_std_dev'}, inplace=True)

# 根据 year_month 进行合并
df = pd.merge(amplitude_df, coherence_df, on='year_month')

# 选择需要的数据
data = df[['coherence_mean', 'amplitude_mean']]

# 应用 KMeans 聚类
kmeans = KMeans(n_clusters=4, random_state=2).fit(data)
df['cluster'] = kmeans.labels_
df['date'] = pd.to_datetime(df['year_month'])

# 绘制散点图
plt.figure(figsize=(20, 16))
scatter = plt.scatter(df['coherence_mean'], df['amplitude_mean'], c=df['cluster'], cmap='viridis', marker='o')

# 在散点上标注日期
for i, row in df.iterrows():
    plt.annotate(f"{row['date'].strftime('%m')}",
                 (row['coherence_mean'], row['amplitude_mean']),
                 textcoords="offset points",
                 xytext=(0, 3),
                 ha='center',
                 fontsize=18)

plt.xlabel('VV Coherence Mean', fontsize=20)
plt.ylabel('VV Amplitude Mean', fontsize=20)
plt.title('KMeans Clustering of Wheat VV Coherence and Amplitude', fontsize=18)
cbar = plt.colorbar(scatter, label='Cluster')
cbar.ax.tick_params(labelsize=18)
cbar.set_label('Cluster', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)
output_file = os.path.join(r'D:\BaiduNetdiskDownload\2023\coherence_amplitude', 'Wheat_VV_coherence_amplitude_kmeans_scatter.png')
plt.savefig(output_file)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# 读取Excel文件
amplitude_file = r'D:\BaiduNetdiskDownload\2023\Winter_wheat_result_all\VH_amplitude_all_monthly.xlsx'
coherence_file = r'D:\BaiduNetdiskDownload\2023\Winter_wheat_result_all\VH_Coherence_all_monthly.xlsx'

amplitude_df = pd.read_excel(amplitude_file)
coherence_df = pd.read_excel(coherence_file)

# 重命名列以便合并
amplitude_df.rename(columns={'mean_value': 'amplitude_mean', 'std_dev_mean': 'amplitude_std_dev'}, inplace=True)
coherence_df.rename(columns={'mean_value': 'coherence_mean', 'std_dev_mean': 'coherence_std_dev'}, inplace=True)

# 根据 year_month 进行合并
df = pd.merge(amplitude_df, coherence_df, on='year_month')

# 选择需要的数据
data = df[['coherence_mean', 'amplitude_mean']]

# 应用 KMeans 聚类
kmeans = KMeans(n_clusters=4, random_state=2).fit(data)
df['cluster'] = kmeans.labels_
df['date'] = pd.to_datetime(df['year_month'])

# 绘制散点图
plt.figure(figsize=(20, 16))
scatter = plt.scatter(df['coherence_mean'], df['amplitude_mean'], c=df['cluster'], cmap='viridis', marker='o')

# 在散点上标注日期
for i, row in df.iterrows():
    plt.annotate(f"{row['date'].strftime('%m')}",
                 (row['coherence_mean'], row['amplitude_mean']),
                 textcoords="offset points",
                 xytext=(0, 3),
                 ha='center',
                 fontsize=18)

plt.xlabel('VH Coherence Mean', fontsize=20)
plt.ylabel('VH Amplitude Mean', fontsize=20)
plt.title('KMeans Clustering of Wheat VH Coherence and Amplitude', fontsize=18)
cbar = plt.colorbar(scatter, label='Cluster')
cbar.ax.tick_params(labelsize=18)
cbar.set_label('Cluster', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)
output_file = os.path.join(r'D:\BaiduNetdiskDownload\2023\coherence_amplitude', 'Wheat_VH_coherence_amplitude_kmeans_scatter.png')
plt.savefig(output_file)
plt.show()

















