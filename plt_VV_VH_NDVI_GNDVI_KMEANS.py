import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.lines import Line2D
# Read GNDVI and NDVI data
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\winter_wheat_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# Read VH data
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# Read VV data
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# Convert date format
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# Extract year and month from date
gndvi_ndvi_data['Year_Month'] = gndvi_ndvi_data['Date'].dt.to_period('M')
vh_data['Year_Month'] = vh_data['date'].dt.to_period('M')
vv_data['Year_Month'] = vv_data['date'].dt.to_period('M')

# Group and aggregate data
gndvi_ndvi_monthly_stats = gndvi_ndvi_data.groupby('Year_Month').agg(
    mean_value_gndvi=('GNDVI_Mean', 'mean'),
    std_dev_gndvi=('GNDVI_Stdev', 'mean'),
    mean_value_ndvi=('NDVI_Mean', 'mean'),
    std_dev_ndvi=('NDVI_Stdev', 'mean')
).reset_index()
vh_monthly_stats = vh_data.groupby('Year_Month')['mean'].agg(
    mean_value_vh='mean',
    std_dev_vh='std'
).reset_index()
vv_monthly_stats = vv_data.groupby('Year_Month')['mean'].agg(
    mean_value_vv='mean',
    std_dev_vv='std'
).reset_index()

# Perform K-means clustering on NDVI, GNDVI, VH, and VV statistics
kmeans_ndvi = KMeans(n_clusters=4, random_state=2).fit(gndvi_ndvi_monthly_stats[['mean_value_ndvi', 'std_dev_ndvi']])
kmeans_gndvi = KMeans(n_clusters=4, random_state=2).fit(gndvi_ndvi_monthly_stats[['mean_value_gndvi', 'std_dev_gndvi']])
kmeans_vh = KMeans(n_clusters=4, random_state=2).fit(vh_monthly_stats[['mean_value_vh', 'std_dev_vh']])
kmeans_vv = KMeans(n_clusters=4, random_state=2).fit(vv_monthly_stats[['mean_value_vv', 'std_dev_vv']])

# Assign cluster labels
gndvi_ndvi_monthly_stats['ndvi_cluster'] = kmeans_ndvi.labels_
gndvi_ndvi_monthly_stats['gndvi_cluster'] = kmeans_gndvi.labels_
vh_monthly_stats['vh_cluster'] = kmeans_vh.labels_
vv_monthly_stats['vv_cluster'] = kmeans_vv.labels_
print(gndvi_ndvi_monthly_stats)
# Create the plot
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)

plt.plot(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
         label='GNDVI Mean', color='green', marker=None, linewidth=0.8)

# Plot NDVI mean as a line plot
plt.plot(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
         label='NDVI Mean', color='blue', marker=None, linewidth=0.8)

# Define cluster colors
colors = ['red', 'green', 'blue', 'purple']

# Scatter NDVI with clusters
plt.scatter(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
            c=gndvi_ndvi_monthly_stats['ndvi_cluster'], cmap='viridis', marker='o')

# Scatter GNDVI with clusters
scatter=plt.scatter(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
            c=gndvi_ndvi_monthly_stats['gndvi_cluster'], cmap='viridis', marker='o')

print(scatter)
# Set x-axis ticks to months
plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
date_ticks = pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
plt.yticks(fontsize=14)

plt.ylim(0, 1)
plt.title('NDVI, GNDVI Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
plt.legend(loc='upper right', fontsize=14, frameon=False, bbox_to_anchor=(1, 0.96))
cbar = plt.colorbar(scatter)
cbar.set_label('Cluster', fontsize=16)
cbar.ax.tick_params(labelsize=14)
# Show plot
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\kmeans_wheat_NDVI_GNDVI_monthly_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()

# Create the plot
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)

# plt.plot(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
#          label='GNDVI Mean', color='green', marker=None, linewidth=0.8)
#
# # Plot NDVI mean as a line plot
# plt.plot(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
#          label='NDVI Mean', color='blue', marker=None, linewidth=0.8)

#Plot VH mean as a line plot
plt.plot(vh_monthly_stats['Year_Month'].dt.to_timestamp(), vh_monthly_stats['mean_value_vh'],
         label='VH Amplitude Mean', color='green', marker=None, linewidth=0.8)

# Plot VV mean as a line plot
plt.plot(vv_monthly_stats['Year_Month'].dt.to_timestamp(), vv_monthly_stats['mean_value_vv'],
         label='VV Amplitude Mean', color='blue', marker=None, linewidth=0.8)
# Define cluster colors
colors = ['red', 'green', 'blue', 'purple']

# # Scatter NDVI with clusters
# plt.scatter(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
#             c=gndvi_ndvi_monthly_stats['ndvi_cluster'], cmap='viridis', marker='o')
#
# # Scatter GNDVI with clusters
# scatter=plt.scatter(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
#             c=gndvi_ndvi_monthly_stats['gndvi_cluster'], cmap='viridis', marker='o')

# Scatter VH with clusters
scattter1=plt.scatter(vh_monthly_stats['Year_Month'].dt.to_timestamp(), vh_monthly_stats['mean_value_vh'],
            c=vh_monthly_stats['vh_cluster'], cmap='viridis', marker='o')

# Scatter VV with clusters
scatter = plt.scatter(vv_monthly_stats['Year_Month'].dt.to_timestamp(), vv_monthly_stats['mean_value_vv'],
            c=vv_monthly_stats['vv_cluster'], cmap='viridis', marker='o')
print(scatter)
# Set x-axis ticks to months
plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
date_ticks = pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
plt.yticks(fontsize=14)

plt.ylim( 2, 5)
plt.title('VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
plt.legend(loc='upper right', fontsize=14, frameon=False, bbox_to_anchor=(1, 0.96))
cbar = plt.colorbar(scatter)
cbar.set_label('Cluster', fontsize=16)
cbar.ax.tick_params(labelsize=14)
# Show plot
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\kmeans_wheat_VV_VH_amplitude_monthly_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()



















