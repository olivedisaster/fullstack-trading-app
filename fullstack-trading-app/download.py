import yfinance

df = yfinance.download("AAPL", start='2022-01-01', end='2022-07-1')
df.to_csv('AAPL.csv')