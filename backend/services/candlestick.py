import matplotlib.pyplot as plt  # The conventional alias is 'plt'
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

def custom_candlestick(ax, opens, closes, highs, lows, dates):
    for i, (o, c, h, l, d) in enumerate(zip(opens, closes, highs, lows, dates)):
        is_up = c >= o
        color = 'green' if is_up else 'red'
        
        # Plot the whiskers (high-low line)
        ax.vlines(i, l, h, color='black', linewidth=1)
        
        # Plot the candlestick body (open-close)
        body_height = abs(o - c)
        body_bottom = min(o, c)
        ax.add_patch(plt.Rectangle((i-0.25, body_bottom), 0.5, body_height, 
                                 fill=True, color=color))

def plot_stock_data(data, period='M'):
    # Create figure
    fig, ax = plt.subplots(figsize=(15, 8))
    
    # Filter last 3 years of data
    three_years_ago = datetime.now() - relativedelta(years=3)
    data = data[data.index >= three_years_ago]
    
    # Monthly view
    grouped_data = data.resample('M').agg({
        '1. open': 'first',
        '4. close': 'last',
        '2. high': 'max',
        '3. low': 'min'
    })
    title = 'Monthly (Last 3 Years)'
    
    custom_candlestick(ax, 
                    grouped_data['1. open'].values,
                    grouped_data['4. close'].values,
                    grouped_data['2. high'].values,
                    grouped_data['3. low'].values,
                    grouped_data.index)
    
    plt.title(f'NVIDIA Stock Price Distribution ({title})', fontsize=16)
    plt.ylabel('Price in USD', fontsize=12)
    plt.xlabel('Date', fontsize=12)
    
    # Format x-axis with months and years
    plt.xticks(range(len(grouped_data)), 
               [d.strftime('%Y-%m') for d in grouped_data.index],
               rotation=45)
    
    plt.tight_layout()
    plt.show()

try:
    # Read and prepare data
    data = pd.read_csv('nvidia_stock_data.csv', index_col=0)
    data.index = pd.to_datetime(data.index)
    data = data.sort_index()
    
    # Plot monthly data
    plot_stock_data(data, 'M')

except FileNotFoundError:
    print("Error: nvidia_stock_data.csv not found. Please run stock.py first to generate the data file.")
except Exception as e:
    print(f"Error creating candlestick chart: {e}")