import pandas as pd
import matplotlib.pyplot as plt

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
print(gndvi_ndvi_data)

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

# Create plot for GNDVI
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
             label='GNDVI Mean', color='green', fmt='-o')

# Create plot for NDVI
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
              label='NDVI Mean', color='blue', fmt='-o')

# Create plot for VH
plt.errorbar(vh_monthly_stats['Year_Month'].dt.to_timestamp(), vh_monthly_stats['mean_value_vh'],
             label='VH Amplitude Mean', color='red', fmt='-o')

# Create plot for VV
plt.errorbar(vv_monthly_stats['Year_Month'].dt.to_timestamp(), vv_monthly_stats['mean_value_vv'],
              label='VV Amplitude Mean', color='purple', fmt='-o')

# Set x-axis ticks to months
plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
date_ticks = pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
plt.yticks( fontsize=14)

plt.ylim(0, 5)
plt.title('NDVI, GNDVI, VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.2))
# Show plot
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_amplitude_monthly_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read GNDVI and NDVI data
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\winter_wheat_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# Read VH data
vh_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VH_Coherence_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# Read VV data
vv_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\VV_Coherence_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# Convert date format
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# Extract year and month from date
gndvi_ndvi_data['Year_Month'] = gndvi_ndvi_data['Date'].dt.to_period('M')
vh_data['Year_Month'] = vh_data['date'].dt.to_period('M')
vv_data['Year_Month'] = vv_data['date'].dt.to_period('M')
print(gndvi_ndvi_data)

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

# Create plot for GNDVI
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
             label='GNDVI Mean', color='green', fmt='-o')

# Create plot for NDVI
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
              label='NDVI Mean', color='blue', fmt='-o')

# Create plot for VH
plt.errorbar(vh_monthly_stats['Year_Month'].dt.to_timestamp(), vh_monthly_stats['mean_value_vh'],
             label='VH Coherence Mean', color='red', fmt='-o')

# Create plot for VV
plt.errorbar(vv_monthly_stats['Year_Month'].dt.to_timestamp(), vv_monthly_stats['mean_value_vv'],
              label='VV Coherence Mean', color='purple', fmt='-o')

# Set x-axis ticks to months
plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
date_ticks = pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
plt.yticks( fontsize=14)

plt.ylim(0,1 )
plt.title('NDVI, GNDVI, VH, and VV Coherence Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))
# Show plot
output_file_path = r'D:\BaiduNetdiskDownload\2023\wheat\wheat_coherence_monthly_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read GNDVI and NDVI data
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\winter_Barley_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# Read VH data
vh_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VH_amplitude_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# Read VV data
vv_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VV_amplitude_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# Convert date format
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# Extract year and month from date
gndvi_ndvi_data['Year_Month'] = gndvi_ndvi_data['Date'].dt.to_period('M')
vh_data['Year_Month'] = vh_data['date'].dt.to_period('M')
vv_data['Year_Month'] = vv_data['date'].dt.to_period('M')
print(gndvi_ndvi_data)

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

# Create plot for GNDVI
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
             label='GNDVI Mean', color='green', fmt='-o')

# Create plot for NDVI
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
              label='NDVI Mean', color='blue', fmt='-o')

# Create plot for VH
plt.errorbar(vh_monthly_stats['Year_Month'].dt.to_timestamp(), vh_monthly_stats['mean_value_vh'],
             label='VH Amplitude Mean', color='red', fmt='-o')

# Create plot for VV
plt.errorbar(vv_monthly_stats['Year_Month'].dt.to_timestamp(), vv_monthly_stats['mean_value_vv'],
              label='VV Amplitude Mean', color='purple', fmt='-o')

# Set x-axis ticks to months
plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
date_ticks = pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
plt.yticks( fontsize=14)

plt.ylim(0, 5)
plt.title('NDVI, GNDVI, VH, and VV Amplitude Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='lower right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.2))
# Show plot
output_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\Barley_amplitude_monthly_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Read GNDVI and NDVI data
gndvi_ndvi_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\winter_Barley_GNDVI_NDVI_2023.csv'
gndvi_ndvi_data = pd.read_csv(gndvi_ndvi_file_path)

# Read VH data
vh_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VH_Coherence_all.xlsx'
vh_data = pd.read_excel(vh_file_path)

# Read VV data
vv_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\VV_Coherence_all.xlsx'
vv_data = pd.read_excel(vv_file_path)

# Convert date format
gndvi_ndvi_data['Date'] = pd.to_datetime(gndvi_ndvi_data['Date'])
vh_data['date'] = pd.to_datetime(vh_data['date'])
vv_data['date'] = pd.to_datetime(vv_data['date'])

# Extract year and month from date
gndvi_ndvi_data['Year_Month'] = gndvi_ndvi_data['Date'].dt.to_period('M')
vh_data['Year_Month'] = vh_data['date'].dt.to_period('M')
vv_data['Year_Month'] = vv_data['date'].dt.to_period('M')
print(gndvi_ndvi_data)

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

# Create plot for GNDVI
plt.figure(figsize=(12, 9))
plt.subplots_adjust(bottom=0.15)
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_gndvi'],
             label='GNDVI Mean', color='green', fmt='-o')

# Create plot for NDVI
plt.errorbar(gndvi_ndvi_monthly_stats['Year_Month'].dt.to_timestamp(), gndvi_ndvi_monthly_stats['mean_value_ndvi'],
              label='NDVI Mean', color='blue', fmt='-o')

# Create plot for VH
plt.errorbar(vh_monthly_stats['Year_Month'].dt.to_timestamp(), vh_monthly_stats['mean_value_vh'],
             label='VH Coherence Mean', color='red', fmt='-o')

# Create plot for VV
plt.errorbar(vv_monthly_stats['Year_Month'].dt.to_timestamp(), vv_monthly_stats['mean_value_vv'],
              label='VV Coherence Mean', color='purple', fmt='-o')

# Set x-axis ticks to months
plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
date_ticks = pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS')  # MS: month start
date_labels = [date.strftime('%Y-%m') for date in date_ticks]
plt.xticks(date_ticks, date_labels, rotation=45, fontsize=14)
plt.yticks( fontsize=14)

plt.ylim(0, 1)
plt.title('NDVI, GNDVI, VH, and VV Coherence Variation Over Time in 2023', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Index Value', fontsize=16)
# plt.legend(loc='lower right', fontsize=14)
plt.legend(loc='upper right', fontsize=16, frameon=False, bbox_to_anchor=(1, 0.96))
# Show plot
output_file_path = r'D:\BaiduNetdiskDownload\2023\Barley\Barley_coherence_monthly_over_time.jpg'
plt.savefig(output_file_path, format='jpg', dpi=300)
plt.show()