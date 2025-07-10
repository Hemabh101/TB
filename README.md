# TB
SMA – Simple Moving Average
Definition:

SMA stands for Simple Moving Average, which is the average of the closing prices over a certain number of periods.

Formula:
For a period of N days:
![image](https://github.com/user-attachments/assets/639249b6-917c-4dce-9687-b35dbe21ba8d)
here P1,P2 .... Pn = closing price of each day 
N= number of days

For example:
| Day | Closing Price (\$) |
| --- | ------------------ |
| 1   | 30,000             |
| 2   | 31,000             |
| 3   | 32,000             |
| 4   | 33,000             |
| 5   | 34,000             |
Then SMA5 (5-day SMA) = (30,000 + 31,000 + 32,000 + 33,000 + 34,000) / 5 = $32,000.
Why is SMA used in trading?
1)Smooths out short-term fluctuations to reveal overall trend
2)Helps identify support and resistance levels
3)Forms the basis for many trading strategies like crossover signals (short SMA crossing above long SMA indicates a bullish trend)



SMA STRATEGY USED:
1. Long-term strategy (50-day SMA vs 200-day SMA crossover)
 How it works:

SMA50 (short-term): 50-day Simple Moving Average, captures medium trend

SMA200 (long-term): 200-day Simple Moving Average, captures broader market trend

 Buy Signal: when SMA50 crosses above SMA200 → bullish crossover
 Sell Signal: when SMA50 crosses below SMA200 → bearish crossover

 Why this works (theory):

Filters out daily market noise

Captures large bullish trends, avoiding false short-term signals

Very popular among institutional investors (called Golden Cross / Death Cross strategy)

 Limitations:

Slow response time → misses early parts of new trends

Generates few trades (good for low transaction costs)

 Typical use case:

Passive portfolios

Long-term position traders or crypto holders who prefer less screen time

2. Medium-term strategy (5-day SMA vs 20-day SMA crossover)
 How it works:

SMA5 (short-term): 5-day average captures quick trend shifts (roughly 1 trading week)

SMA20 (medium-term): 20-day average captures a month’s trend

 Buy Signal: when SMA5 crosses above SMA20
 Sell Signal: when SMA5 crosses below SMA20

 Why this works (theory):

Balances between reactivity and noise reduction

Provides more frequent trades than long-term SMA strategies

Captures swings within monthly trends effectively

 Limitations:

More trades → higher potential transaction costs and slippage

May get whipsawed in sideways markets (false signals when price moves horizontally)

 Typical use case:

Swing traders

Medium-term crypto or equity traders looking for weekly opportunities

Algorithmic trading bots with automated execution to handle frequency efficiently


3. Short-term / Daily strategy (1-day SMA vs 2-day SMA crossover)
 How it works:

SMA1: essentially the closing price of the day

SMA2: 2-day average smooths just slightly

 Buy Signal: when today’s price moves above the average of today & yesterday
 Sell Signal: when it dips below

 Why this works (theory):

Generates frequent buy/sell signals → almost daily trades

Attempts to capture micro price movements for scalping profits

Suitable for high-frequency algorithmic traders with negligible transaction costs

 Limitations:

Extremely prone to noise and false signals

Trading fees can eat away profits quickly

Requires tight risk management, rapid execution, and often large capital for micro-gains

 Typical use case:

Intraday scalpers

Automated bots connected to exchanges like Binance/Alpaca

NOT suitable for manual trading due to rapid signal changes

Summary:
| **Strategy**           | **Windows**       | **Frequency**              | **Best for**                             | **Risks**                         |
| ---------------------- | ----------------- | -------------------------- | ---------------------------------------- | --------------------------------- |
| **Long-term**          | 50-day vs 200-day | Very low (few trades/year) | Passive investors, portfolio rebalancing | Miss early trend reversals        |
| **Medium-term**        | 5-day vs 20-day   | Medium (few trades/month)  | Swing traders, weekly trades             | False signals in sideways market  |
| **Short-term / Daily** | 1-day vs 2-day    | Very high (daily)          | Scalpers, HFT bots                       | High noise, high transaction cost |
 
