import pandas as pd
import matplotlib.pyplot as plt

#this is for short term 5-day vs 20-day SMA trades 

# ==========================
# 1. Load and clean the CSV
# ==========================
df = pd.read_csv('BTC_2023.csv', header=0)

# Flatten multi-level columns if they exist
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [' '.join(col).strip() for col in df.columns.values]

# Strip column names
df.columns = df.columns.str.strip()

# Rename to remove ' BTC-USD' suffix
df.columns = [col.split()[0] for col in df.columns]

# Convert 'Date' to datetime
if 'Date' not in df.columns:
    raise ValueError("Column 'Date' not found. Check your CSV header.")

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df.set_index('Date', inplace=True)

# Convert Close to numeric
if 'Close' not in df.columns:
    raise ValueError("'Close' column missing after renaming. Check column names.")

df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df = df.dropna(subset=['Close'])

# Check DataFrame is not empty
if df.empty:
    raise ValueError("DataFrame is empty after cleaning. Check CSV content.")

# =====================================
# 2. Calculate Moving Averages & Signal
# =====================================
short_window = 5    # Short-term SMA (e.g. 5-day)
long_window = 20    # Longer short-term SMA (e.g. 20-day)

df['SMA5'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['SMA20'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate signals
df['Signal'] = (df['SMA5'] > df['SMA20']).astype(int)
df['Position'] = df['Signal'].diff()

# ==========================
# 3. Backtesting simulation
# ==========================
initial_capital = 10000
btc_holding = 0
cash = initial_capital
positions = []
trade_results = []

for i in range(len(df)):
    if df['Position'].iloc[i] == 1:  # Buy
        btc_holding = cash / df['Close'].iloc[i]
        buy_price = df['Close'].iloc[i]
        cash = 0
        positions.append(('BUY', df.index[i], buy_price))
    elif df['Position'].iloc[i] == -1 and btc_holding > 0:  # Sell
        sell_price = df['Close'].iloc[i]
        cash = btc_holding * sell_price
        btc_holding = 0
        positions.append(('SELL', df.index[i], sell_price))
        trade_results.append(sell_price - buy_price)

# Final portfolio value
final_value = cash + btc_holding * df['Close'].iloc[-1]
profit = final_value - initial_capital

# ==========================
# 4. Results and accuracy
# ==========================
print(f"Final portfolio value: ${final_value:.2f}")
print(f"Net profit: ${profit:.2f}")
print("Trade History:")
for p in positions:
    print(p)

# Accuracy calculation
if trade_results:
    profitable_trades = sum([1 for x in trade_results if x > 0])
    accuracy = profitable_trades / len(trade_results) * 100
    print(f"Total trades: {len(trade_results)}")
    print(f"Profitable trades: {profitable_trades}")
    print(f"Accuracy: {accuracy:.2f}%")
else:
    print("No completed trades to calculate accuracy.")

# ==========================
# 5. Plotting
# ==========================
plt.figure(figsize=(14,7))
plt.plot(df['Close'], label='BTC Close Price', alpha=0.5)
plt.plot(df['SMA5'], label='SMA5', alpha=0.9)
plt.plot(df['SMA20'], label='SMA20', alpha=0.9)

# Buy signals
plt.plot(df[df['Position'] == 1].index,
         df['Close'][df['Position'] == 1],
         '^', markersize=10, color='g', label='Buy Signal')

# Sell signals
plt.plot(df[df['Position'] == -1].index,
         df['Close'][df['Position'] == -1],
         'v', markersize=10, color='r', label='Sell Signal')

plt.title('BTC Short-Term Moving Average Crossover Strategy Backtest (2023)')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid()
plt.show()
