import os
import rasterio
from rasterio.mask import mask
from osgeo import ogr
import geopandas as gpd
import numpy as np
import math
import warnings
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

warnings.filterwarnings("ignore", category=UserWarning)

# Define the file paths
shp_file_path = 'G:/2023 Crop/Crop_2023/Winter_Barley_2023.shp'
dbf_file_path = 'G:/2023 Crop/Crop_2023/Winter_Barley_2023.dbf'

# Open the shapefile
ds = ogr.Open(shp_file_path)
if ds is None:
    raise Exception("Could not open the shapefile")

# Get the first (and presumably only) layer
layer = ds.GetLayer(0)

# Fetch some basic information about the shapefile
feature_count = layer.GetFeatureCount()
layer_defn = layer.GetLayerDefn()
field_names = [layer_defn.GetFieldDefn(i).GetName() for i in range(layer_defn.GetFieldCount())]

# Extracting a sample of features' attribute data
sample_data = []
for i in range(min(5, feature_count)):  # Limit to 5 for preview
    feature = layer.GetFeature(i)
    attributes = {field: feature.GetField(field) for field in field_names}
    sample_data.append(attributes)

# Load the shapefile
gdf = gpd.read_file(shp_file_path)

# Display basic information about the GeoDataFrame
info = {
    "Number of features": len(gdf),
    "Columns": gdf.columns.tolist(),
    "Sample data": gdf.head().to_dict(orient="records")  # Convert the first few rows to a dictionary for easy viewing
}

# Print the information for debugging
print(info)

# Define the directory containing TIF files
tif_directory_path = 'C:/Users/Windows/Desktop/2023/VH_Coherence'

# List all TIF files in the directory
file_names = [os.path.join(tif_directory_path, f) for f in os.listdir(tif_directory_path) if f.endswith('.tif')]

# Function to calculate mean and std of pixel values for each geometry
def calculate_stats_for_all_geometries(geometries, raster_path):
    stats = []
    with rasterio.open(raster_path) as src:
        for geom in geometries:
            out_image, out_transform = mask(src, [geom], crop=True, nodata=src.nodata)
            masked_data = np.ma.masked_array(out_image, mask=(out_image == src.nodata))
            if np.ma.count(masked_data) > 0:  # Check there is data
                fixed_data = np.array([x for x in list(np.array(masked_data).reshape(-1)) if not math.isnan(x)])
                if len(fixed_data) == 0:
                    mean_val = std_val = np.nan
                else:
                    mean_val = fixed_data.mean()
                    std_val = fixed_data.std()
            else:
                mean_val = std_val = np.nan  # Assign NaN if no valid data
            stats.append({"mean": mean_val, "std": std_val})
    return stats

# Function to sample raster values at given points
def sample_raster_at_points(raster_path, points):
    with rasterio.open(raster_path) as src:
        # Transform points to the raster's CRS
        points_transformed = points.to_crs(src.crs)
        # Sample the raster at the given points
        sampled_values = [x[0] for x in src.sample([(pt.x, pt.y) for pt in points_transformed.geometry])]
    return sampled_values

mean_datas = [[],[]]
std_datas = [[],[]]
dates = [[],[]]


for filename in file_names:
    # Define the path to the TIF file
    str = filename.split('_')
    date = str[-1][:-4]
    date = date.split('t')[0]
    date = date[0:4]+'-'+date[4:6]+'-'+date[6:8]
    isDecending = False
    for s in str:
        if s == '1':
            isDecending = True
        elif s == '2':
            isDecending = False
        elif s == '3':
            isDecending = False
        elif s == '4':
            isDecending = True
    
    # Open the TIF file to read its properties
    with rasterio.open(filename) as src:
        tif_crs = src.crs
        tif_bounds = src.bounds
        tif_meta = src.meta

    # Reproject the shapefile to match the TIF file's CRS
    gdf_reprojected = gdf.to_crs(tif_crs)

    # Calculate centroids of the geometries in the GeoDataFrame
    gdf_reprojected['centroid'] = gdf_reprojected.geometry.centroid

    # Sample the raster at the centroids of the geometries
    sampled_values = sample_raster_at_points(filename, gdf_reprojected['centroid'])

    # Add the sampled raster values to the GeoDataFrame
    gdf_reprojected['raster_value'] = sampled_values

    # Filter out NaN values for mean and std calculation
    fixed_values = np.array([x for x in sampled_values if not math.isnan(x)])
    mean_value = fixed_values.mean()
    std_value = fixed_values.std()
    
    mean_datas[isDecending].append(mean_value)
    std_datas[isDecending].append(std_value)
    dates[isDecending].append(date)


mean_plus_std = [[mean + std for mean, std in zip(mean_datas[i], std_datas[i])] for i in range(2)]
mean_minus_std = [[mean - std for mean, std in zip(mean_datas[i], std_datas[i])] for i in range(2)]

# 生成2023年每天的日期
all_dates = pd.date_range(start='2023-01-01', end='2023-12-31')

# # 生成部分日期的数据，例如每月的第一天
# sparse_dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS')
# values = np.random.randint(10, 100, size=len(sparse_dates))

# 创建一个完整日期范围的DataFrame，并将值填充到相应日期
for i in range(2):
    df = pd.DataFrame({'Date': all_dates})
    df['Value'] = np.nan  # 初始化为NaN
    df['Value1'] = np.nan  # 初始化为NaN
    df['Value2'] = np.nan  # 初始化为NaN
    df['Var'] = np.nan  # 初始化为NaN
    df.loc[df['Date'].isin(dates[i]), 'Value'] = mean_datas[i]
    df.loc[df['Date'].isin(dates[i]), 'Value1'] = mean_plus_std[i]
    df.loc[df['Date'].isin(dates[i]), 'Value2'] = mean_minus_std[i]
    df.loc[df['Date'].isin(dates[i]), 'Var'] = std_datas[i]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.errorbar(df['Date'], df['Value'], yerr=df['Var'], fmt='o', capsize=5)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    fig.autofmt_xdate()

    plt.xlabel('Time')
    plt.xticks(rotation=90)
    plt.ylabel('Mean')
    plt.title('Mean Values with Error Bars of ' + ('Decending' if i else 'Ascending'))
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Date'], df['Value'], color='red', marker='^')
    ax.scatter(df['Date'], df['Value2'], color='blue', marker='^')
    ax.scatter(df['Date'], df['Value1'], color='blue', marker='^')

    # 填充缺失值，使用线性插值
    df['Value'] = df['Value'].interpolate(method='linear')
    df['Value1'] = df['Value1'].interpolate(method='linear')
    df['Value2'] = df['Value2'].interpolate(method='linear')
    
    ax.plot(df['Date'], df['Value'], color='red', linestyle='-', marker='', linewidth=2, label='Mean')
    ax.plot(df['Date'], df['Value2'], color='blue', linestyle='--', marker='', linewidth=1, label='Mean - Std')
    ax.plot(df['Date'], df['Value1'], color='blue', linestyle='--', marker='', linewidth=1, label='Mean + Std')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    fig.autofmt_xdate()
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.title('Decending' if i else 'Ascending')
    plt.grid(True)
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    plt.show()
    
    