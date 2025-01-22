import pandas as pd
import matplotlib.pyplot as plt

# Sample data in the provided CSV format
with open("sp500_index.csv", 'r') as f:
    # Read the data into a pandas DataFrame
    df = pd.read_csv(f, parse_dates=['Date'])

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['S&P500'], marker='o')
    plt.title('S&P 500 Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('S&P 500 Price')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()
