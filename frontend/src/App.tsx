import { useState, ChangeEvent } from 'react'
import { StockChart } from './components/StockChart'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'

export const App = () => {
  // 获取当前日期
  const today = new Date()
  
  // 获取当月1日
  const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1)
  
  // 设置状态默认值
  const [interval, setInterval] = useState<'1d' | '1w' | '1m' | '1y'>('1d')
  const [startDate, setStartDate] = useState<Date>(firstDayOfMonth)
  const [endDate, setEndDate] = useState<Date>(today)

  const handleIntervalChange = (e: ChangeEvent<HTMLSelectElement>) => {
    setInterval(e.target.value as '1d' | '1w' | '1m' | '1y')
  }

  return (
    <div className="container mx-auto p-4">
      <div className="mb-12">  {/* 增加底部间距 */}
        <div className="flex items-center space-x-8">
          <div className="flex-none">
            <select 
              value={interval} 
              onChange={handleIntervalChange}
              className="border p-2 rounded bg-white shadow-sm"
            >
              <option value="1d">日K</option>
              <option value="1w">周K</option>
              <option value="1m">月K</option>
              <option value="1y">年K</option>
            </select>
          </div>
          
          <div className="flex items-center space-x-4">
            <DatePicker
              selected={startDate}
              onChange={setStartDate}
              placeholderText="开始日期"
              className="border p-2 rounded bg-white shadow-sm"
              dateFormat="yyyy-MM-dd"
              maxDate={endDate}
            />
            
            <span className="text-gray-500">至</span>
            
            <DatePicker
              selected={endDate}
              onChange={setEndDate}
              placeholderText="结束日期"
              className="border p-2 rounded bg-white shadow-sm"
              dateFormat="yyyy-MM-dd"
              minDate={startDate}
              maxDate={today}
            />
          </div>
        </div>
      </div>
      
      <StockChart 
        symbol="NVDA"
        interval={interval}
        startDate={startDate?.toISOString().split('T')[0]}
        endDate={endDate?.toISOString().split('T')[0]}
      />
    </div>
  )
}