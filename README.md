 HEAD
# 📊 Bitcoin Market Sentiment vs Trader Performance Analysis

## Overview

This project analyzes the relationship between **Bitcoin Market Sentiment (Fear & Greed Index)** and **Hyperliquid traders' performance**. The objective is to discover patterns between market psychology and trading profitability using exploratory data analysis (EDA) and data visualization.

---

## Objectives

- Clean and preprocess both datasets.
- Merge trader data with Bitcoin Fear & Greed Index.
- Analyze trader profitability under different market sentiments.
- Visualize important trends and trading behavior.
- Generate business insights for smarter trading strategies.

---

## Datasets

### 1. Historical Trader Data
Contains:
- Account
- Coin
- Execution Price
- Side (BUY/SELL)
- Size
- Closed PnL
- Fee
- Timestamp
- Order ID
- Trade ID

### 2. Bitcoin Fear & Greed Index
Contains:
- Date
- Market Sentiment Classification
- Fear & Greed Value

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Project Structure

```
bitcoin-sentiment-analysis/
│
├── data/
│   ├── historical_data.csv
│   └── fear_greed.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── outputs/
│   ├── pnl_vs_sentiment.png
│   ├── insights.txt
│   └── final_report.md
│
├── README.md
└── requirements.txt
```

---

## Analysis Performed

- Data Cleaning
- Date Conversion
- Dataset Merging
- Profit Analysis
- Trade Count Analysis
- Sentiment-wise Performance
- Correlation Analysis
- Data Visualization

---

## Visualizations

The notebook includes:

- Closed PnL vs Market Sentiment (Boxplot)
- Trade Count by Sentiment
- Profit Distribution Histogram
- Correlation Heatmap

---

## Key Insights

- Trader profitability changes across different market sentiment categories.
- Fear periods recorded the highest trading activity.
- Buy and Sell trades remain relatively balanced across sentiments.
- Profit distribution contains several outliers, indicating high-risk and high-reward trades.
- Market sentiment provides useful context for evaluating trading performance.

---

## Conclusion

The analysis indicates that market sentiment influences trader behavior and profitability. Combining sentiment indicators with trading data can support more informed trading decisions and improved risk management.

---

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Open the notebook

```
notebooks/analysis.ipynb
```

4. Run all cells.

---

## Author

**Dhairya Thakur**