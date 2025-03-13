# Stock Review - Real-time Stock Analysis Platform

## 🚀 Features

- 📊 Real-time stock data visualization with candlestick charts
- 📅 Flexible time interval selection (daily/weekly/monthly/yearly)
- 📈 Advanced technical analysis capabilities
- 🔄 Auto-updating data from Alpha Vantage API
- 🎨 Clean and intuitive user interface
- 📱 Responsive design for all devices

## 🛠️ Tech Stack

### Frontend
- React 18 with TypeScript
- Vite for fast development and building
- Lightweight Charts for professional-grade financial charts
- Modern date picker for time range selection

### Backend
- FastAPI for high-performance API
- Pandas for efficient data processing
- Alpha Vantage integration for real-time stock data

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Alpha Vantage API key

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/StockReview.git
cd StockReview/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your Alpha Vantage API key to .env
```

### Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 🚀 Quick Start

1. Start the backend server:
```bash
cd backend
source venv/bin/activate
uvicorn api.stock_api:app --reload --port 8000
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Open `http://localhost:5173` in your browser

## 📊 Usage

1. Select a time interval (daily/weekly/monthly/yearly)
2. Choose date range using the date pickers
3. View the candlestick chart with price movements
4. Analyze trends and patterns in the data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

danielviki - [@danielviki]

Project Link: [https://github.com/yourusername/StockReview](https://github.com/yourusername/StockReview)

## 🙏 Acknowledgments

- [Alpha Vantage](https://www.alphavantage.co/) for providing stock market data
- [Lightweight Charts](https://www.tradingview.com/lightweight-charts/) for the charting library
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing backend framework

---
⭐️ If you found this project helpful, please give it a star!

