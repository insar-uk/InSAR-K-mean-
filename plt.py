import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, MonthLocator
from matplotlib.ticker import MaxNLocator
# 文件路径
excel_dir = r'D:\BaiduNetdiskDownload\2023\Winter_Barley__result'
output_dir = r'D:\BaiduNetdiskDownload\2023\Winter_Barley__result\charts_monthly'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 获取所有的 `_monthly.xlsx` 文件
monthly_files = [f for f in os.listdir(excel_dir) if f.endswith('_monthly.xlsx')]

# 设置 Seaborn 样式
sns.set(style='whitegrid')

# 遍历所有的 `_monthly.xlsx` 文件
for monthly_file in monthly_files:
    # 读取 Excel 文件
    file_path = os.path.join(excel_dir, monthly_file)
    df = pd.read_excel(file_path)

    # 确保 year_month 列为日期格式
    df['year_month'] = pd.to_datetime(df['year_month'])

    # 绘制时间变化图
    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(x='year_month', y='mean_value', data=df, marker='o')

    # 添加标准误差棒
    plt.errorbar(df['year_month'], df['mean_value'], yerr=df['std_dev_mean'], fmt='o', ecolor='gray', capsize=5)

    # 设置标题和标签
    plt.title(f'Monthly Mean Value Over Time - {monthly_file}')
    plt.xlabel('Year-Month')
    plt.ylabel('Mean Value')

    # 设置 x 轴范围和刻度间隔为月份
    plt.xlim(pd.Timestamp('2022-12-15'), pd.Timestamp('2023-12-15'))
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(MonthLocator())

    # 自动调整 y 轴刻度
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # plt.grid(True)
    plt.tight_layout()

    # 保存图像
    output_file = os.path.join(output_dir, f'{os.path.splitext(monthly_file)[0]}.png')
    plt.savefig(output_file)

    # 关闭当前图像
    plt.close()

print("所有图像已保存到:", output_dir)

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, MonthLocator
from matplotlib.ticker import MaxNLocator

# 文件路径
excel_dir = r'D:\BaiduNetdiskDownload\2023\Winter_Barley__result'
output_dir = r'D:\BaiduNetdiskDownload\2023\Winter_Barley__result\charts_daily'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 获取所有的 Excel 文件（未取平均的）
excel_files = [f for f in os.listdir(excel_dir) if f.endswith('.xlsx') and not f.endswith('_monthly.xlsx')]

# 设置 Seaborn 样式
sns.set(style='whitegrid')

# 遍历所有的 Excel 文件
for excel_file in excel_files:
    # 读取 Excel 文件
    file_path = os.path.join(excel_dir, excel_file)
    df = pd.read_excel(file_path)

    # 确保日期列为日期格式
    df['date'] = pd.to_datetime(df['date'])

    # 提取日、月、年信息
    df['year_month'] = df['date'].dt.to_period('M')

    # 绘制时间变化图
    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(x='date', y='mean', data=df, marker='o')

    # 添加标准误差棒
    plt.errorbar(df['date'], df['mean'], yerr=df['std'], fmt='o', ecolor='gray', capsize=5)

    # 设置标题和标签
    plt.title(f'Daily Mean Value Over Time - {excel_file}')
    plt.xlabel('Date')
    plt.ylabel('Mean Value')

    # 设置 x 轴范围和刻度间隔为月份
    plt.xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2023-12-31'))
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(MonthLocator())

    # 自动调整 y 轴刻度
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.grid(True)
    plt.tight_layout()

    # 保存图像
    output_file = os.path.join(output_dir, f'{os.path.splitext(excel_file)[0]}_daily.png')
    plt.savefig(output_file)

    # 关闭当前图像
    plt.close()

print("所有图像已保存到:", output_dir)
