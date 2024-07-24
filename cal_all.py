import os
import rasterio
import geopandas as gpd
import pandas as pd
import numpy as np
from rasterio.mask import mask

# 文件路径
tif_dir = r'D:\BaiduNetdiskDownload\2023\VH_Coherence'
shp_file = r'D:\BaiduNetdiskDownload\Crop_2023\Winter_Barley_2023_pro.shp'
excel_dir = r'D:\BaiduNetdiskDownload\2023\Winter_Barley_result_all'
# 读取 shapefile
os.makedirs(excel_dir, exist_ok=True)
shapefile = gpd.read_file(shp_file)

# 用于存储结果的列表
results_all = []

# 获取所有的 TIFF 文件
tif_files = [f for f in os.listdir(tif_dir) if f.endswith('.tif')]

# 遍历所有的 TIFF 文件
for tif_file in tif_files:
    print(tif_file)
    # 获取完整文件路径
    file_path = os.path.join(tif_dir, tif_file)

    # 解析文件名
    parts = tif_file.split('_')
    stack = parts[3]
    print(stack)
    date_str = parts[6][0:8]  # 获取日期部分
    print(date_str)
    date = pd.to_datetime(date_str, format='%Y%m%d')  # 转换成日期格式



    # 读取 TIFF 文件
    with rasterio.open(file_path) as src:
        # 使用 shapefile 对图像进行裁剪
        out_image, out_transform = mask(src, shapefile.geometry, crop=True)
        out_image = out_image[0]  # 只取第一个 band
        print(out_image)
        # 计算均值和中值
        mean_val = np.mean(out_image[(out_image != src.nodata) & (out_image > 0) & (~np.isnan(out_image))])
        std_val = np.std(out_image[(out_image != src.nodata) & (out_image > 0) & (~np.isnan(out_image))])

    # 将结果添加到相应的列表
    result = [tif_file, date, mean_val, std_val]

    results_all.append(result)



# 获取文件夹名称
folder_name = os.path.basename(tif_dir)

# 将结果保存到 Excel 文件
columns = ['tif_name', 'date', 'mean', 'std']

df_all = pd.DataFrame(results_all, columns=columns)

df_all.to_excel(os.path.join(excel_dir, f'{folder_name}_all.xlsx'), index=False)
print( f'{folder_name}_all.xlsx')