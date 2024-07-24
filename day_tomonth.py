import os
import pandas as pd

# 文件路径
excel_dir = r'D:\BaiduNetdiskDownload\2023\Winter_wheat__result'

# 获取所有的 Excel 文件
excel_files = [f for f in os.listdir(excel_dir) if f.endswith('.xlsx')]

# 遍历所有的 Excel 文件
for excel_file in excel_files:
    # 读取 Excel 文件
    file_path = os.path.join(excel_dir, excel_file)
    df = pd.read_excel(file_path)

    # 确保日期列为日期格式
    df['date'] = pd.to_datetime(df['date'])

    # 提取年月信息
    df['year_month'] = df['date'].dt.to_period('M')

    # 按年月分组，计算 mean 的均值和标准差
    monthly_stats = df.groupby('year_month')['mean'].agg(
        mean_value='mean',
        std_dev_mean='std'
    ).reset_index()

    # 将结果保存到新的 Excel 文件
    new_file_name = excel_file.replace('.xlsx', '_monthly.xlsx')
    new_file_path = os.path.join(excel_dir, new_file_name)

    # 将 monthly_stats 写入新的 Excel 文件
    monthly_stats.to_excel(new_file_path, index=False)
