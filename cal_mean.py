import os
import rasterio
import geopandas as gpd
import pandas as pd
import numpy as np
from rasterio.mask import mask

# 文件路径
tif_dir = r'C:/Users/Windows/Desktop/VH_amplitude'
shp_file = r'G:/2023 Crop/Crop_2023/Winter_Barley_2023.shp'
excel_dir = r'C:/Users/Windows/Desktop/VH_amplitude/Winter_wheat__result'
# 读取 shapefile
os.makedirs(excel_dir, exist_ok=True)
shapefile = gpd.read_file(shp_file)

# 用于存储结果的列表
results_descending = []
results_ascending = []

# 获取所有的 TIFF 文件
tif_files = [f for f in os.listdir(tif_dir) if f.endswith('.tif')]

# 遍历所有的 TIFF 文件
for tif_file in tif_files:
    print(tif_file)
    # 获取完整文件路径
    file_path = os.path.join(tif_dir, tif_file)

    # 解析文件名
    parts = tif_file.split('_')
    stack = parts[2]
    print(stack)
    date_str = parts[5][0:8]  # 获取日期部分
    print(date_str)
    date = pd.to_datetime(date_str, format='%Y%m%d')  # 转换成日期格式

    # 判断是 Descending 还是 Ascending
    if stack in ['1', '4']:
        orbit = 'Descending'
    elif stack in ['2', '3']:
        orbit = 'Ascending'
    else:
        continue  # 如果不符合条件，跳过

    # 读取 TIFF 文件
    with rasterio.open(file_path) as src:
        # 使用 shapefile 对图像进行裁剪
        out_image, out_transform = mask(src, shapefile.geometry, crop=True)
        out_image = out_image[0]  # 只取第一个 band

        # 计算均值和中值
        mean_val = np.mean(out_image[out_image != src.nodata])
        std_val = np.std(out_image[out_image != src.nodata])

    # 将结果添加到相应的列表
    result = [tif_file, date, mean_val, std_val]
    if orbit == 'Descending':
        results_descending.append(result)
    else:
        results_ascending.append(result)

# 获取文件夹名称
folder_name = os.path.basename(tif_dir)

# 将结果保存到 Excel 文件
columns = ['tif_name', 'date', 'mean', 'std']

df_descending = pd.DataFrame(results_descending, columns=columns)
df_ascending = pd.DataFrame(results_ascending, columns=columns)

df_descending.to_excel(os.path.join(excel_dir, f'{folder_name}_Descending.xlsx'), index=False)
print( f'{folder_name}_Descending.xlsx')
df_ascending.to_excel(os.path.join(excel_dir, f'{folder_name}_Ascending.xlsx'), index=False)
