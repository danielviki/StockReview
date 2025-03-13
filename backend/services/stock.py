import os
from dotenv import load_dotenv
try:
    from alpha_vantage.timeseries import TimeSeries
except ModuleNotFoundError:
    print("The 'alpha_vantage' module is not installed. Please install it using 'pip install alpha_vantage'")
    exit()

import pandas as pd

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
if not api_key:
    raise ValueError("API key not found. Please set ALPHA_VANTAGE_API_KEY in .env file")

# Create TimeSeries object
ts = TimeSeries(key=api_key, output_format='pandas')

# 获取 NVIDIA 股票过去一年（365天）的日线数据
data, meta_data = ts.get_daily(symbol='NVDA', outputsize='full')

# 打印数据
print(data.tail())  # 打印最后几行数据，查看最新的股票数据

# 如果你需要保存到 CSV 文件中，可以使用以下代码：
data.to_csv('nvidia_stock_data.csv')
