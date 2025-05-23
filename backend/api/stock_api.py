import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import pandas as pd
import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite 默认端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/stock/{symbol}")
async def get_stock_data(
    symbol: str,
    interval: str = Query("1d", enum=["1d", "1w", "1m", "1y"]),
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    try:
        # 构建文件路径
        base_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "data"))
        file_path = os.path.normpath(os.path.join(base_path, f"{symbol}_stock_data.csv"))
        
        # 验证路径是否在允许的目录中
        if not file_path.startswith(base_path):
            logger.error(f"非法路径访问尝试: {file_path}")
            raise HTTPException(status_code=400, detail="非法路径访问")
        
        logger.debug(f"尝试读取文件: {file_path}")
        
        # 检查文件是否存在
        if not os.path.exists(file_path):
            logger.error(f"文件不存在: {file_path}")
            raise HTTPException(status_code=404, detail=f"未找到 {symbol} 的股票数据文件")
        
        # 读取数据
        data = pd.read_csv(file_path)
        logger.debug(f"成功读取数据，列名: {data.columns}")
        
        # 将日期列设置为索引
        data['date'] = pd.to_datetime(data['date'])
        data = data.set_index('date')
        data = data.sort_index(ascending=True)
        
        logger.debug(f"处理后的数据头部:\n{data.head()}")
        
        # 根据时间间隔重采样数据
        if interval != "1d":
            # 确保日期索引是升序的
            data = data.sort_index(ascending=True)
            
            if interval == "1w":
                # 按周重采样，周一开始
                data = data.resample('W-MON').agg({
                    '1. open': 'first',  # 周一开盘价
                    '4. close': 'last',  # 周五收盘价
                    '2. high': 'max',    # 周内最高价
                    '3. low': 'min',     # 周内最低价
                    '5. volume': 'sum'    # 周成交量之和
                })
            elif interval == "1m":
                # 按月重采样，月初开始
                data = data.resample('M').agg({
                    '1. open': 'first',  # 月初开盘价
                    '4. close': 'last',  # 月末收盘价
                    '2. high': 'max',    # 月内最高价
                    '3. low': 'min',     # 月内最低价
                    '5. volume': 'sum'   # 月成交量之和
                })
            else:  # "1y"
                # 按年重采样，年初开始
                data = data.resample('Y').agg({
                    '1. open': 'first',  # 年初开盘价
                    '4. close': 'last',  # 年末收盘价
                    '2. high': 'max',    # 年内最高价
                    '3. low': 'min',     # 年内最低价
                    '5. volume': 'sum'   # 年成交量之和
                })

        # 过滤日期范围
        if start_date:
            data = data[data.index >= pd.to_datetime(start_date)]
        if end_date:
            data = data[data.index <= pd.to_datetime(end_date)]
            
        logger.debug(f"过滤后的数据范围: {data.index.min()} 到 {data.index.max()}")
        logger.debug(f"数据条数: {len(data)}")
        
        # 转换为列表
        result = []
        for index, row in data.iterrows():
            result.append({
                "date": index.strftime('%Y-%m-%d'),
                "1. open": float(row['1. open']),
                "2. high": float(row['2. high']),
                "3. low": float(row['3. low']),
                "4. close": float(row['4. close']),
                "5. volume": float(row['5. volume'])
            })
        
        logger.debug(f"处理完成，返回 {len(result)} 条数据")
        return result
        
    except Exception as e:
        logger.exception("处理请求时发生错误")
        raise HTTPException(status_code=500, detail=str(e))