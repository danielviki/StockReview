import { useEffect, useRef } from 'react';
import { createChart, IChartApi } from 'lightweight-charts';
import type { StockData } from '../types/chart';

interface StockChartProps {
    symbol: string;
    interval: '1d' | '1w' | '1m' | '1y';
    startDate?: string;
    endDate?: string;
}

export const StockChart = ({ symbol, interval, startDate, endDate }: StockChartProps) => {
    const chartContainerRef = useRef<HTMLDivElement>(null);
    const chartRef = useRef<IChartApi | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                // 清除旧图表
                if (chartRef.current) {
                    chartRef.current.remove();
                    chartRef.current = null;
                }

                // 创建新图表
                if (chartContainerRef.current) {
                    const newChart = createChart(chartContainerRef.current, {
                        width: chartContainerRef.current.clientWidth,
                        height: 500,
                        layout: {
                            background: { color: '#ffffff' },
                            textColor: '#333',
                        },
                        grid: {
                            vertLines: { color: '#f0f0f0' },
                            horzLines: { color: '#f0f0f0' },
                        },
                        timeScale: {
                            timeVisible: true,
                            secondsVisible: false,
                        },
                    });
                    
                    chartRef.current = newChart;
                }

                const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
                console.log('Fetching from:', `${baseUrl}/api/stock/${symbol}`);
                
                const params = new URLSearchParams({
                    interval,
                    ...(startDate && { start_date: startDate }),
                    ...(endDate && { end_date: endDate })
                });
                
                console.log('Fetching data with params:', params.toString());
                
                const response = await fetch(`${baseUrl}/api/stock/${symbol}?${params}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                    },
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                console.log('Received data:', data);
                
                // 转换数据格式并按日期排序
                const chartData: StockData[] = data
                    .map((item: any) => ({
                        time: item.date.split('T')[0],
                        open: Number(item['1. open']),
                        high: Number(item['2. high']),
                        low: Number(item['3. low']),
                        close: Number(item['4. close'])
                    }))
                    .sort((a, b) => new Date(a.time).getTime() - new Date(b.time).getTime());

                console.log('Processed chart data:', chartData);

                if (chartRef.current) {
                    const candlestickSeries = chartRef.current.addCandlestickSeries({
                        upColor: '#26a69a',
                        downColor: '#ef5350',
                        borderVisible: false,
                        wickUpColor: '#26a69a',
                        wickDownColor: '#ef5350'
                    });
                    
                    candlestickSeries.setData(chartData);
                    chartRef.current.timeScale().fitContent();
                }
            } catch (error) {
                console.error('Fetch data failed:', error);
            }
        };

        fetchData();

        return () => {
            if (chartRef.current) {
                chartRef.current.remove();
                chartRef.current = null;
            }
        };
    }, [symbol, interval, startDate, endDate]);
    
    return <div ref={chartContainerRef} style={{ width: '100%', height: '500px', marginTop: '2rem' }} />;
};