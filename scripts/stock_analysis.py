# stock_analysis.py
import os
import numpy as np
import pandas as pd
import talib
import seaborn as sns
import matplotlib.pyplot as plt

def load_stock_data(base_path, stock_files):
    """
    Load multiple stock data into separate DataFrames and combine them into one.
    :param base_path: Path to the directory containing stock data files.
    :param stock_files: Dictionary mapping stock symbols to their CSV file paths.
    :return: A combined DataFrame with all stock data.
    """
    combined_df = pd.DataFrame()
    dataframes = {}

    for symbol, file_path in stock_files.items():
        full_path = os.path.join(base_path, file_path)
        try:
            df = pd.read_csv(full_path, parse_dates=['Date'])
            df['Symbol'] = symbol
            dataframes[symbol] = df
            combined_df = pd.concat([combined_df, df])
            print(f"Loaded {symbol} data successfully.")
        except Exception as e:
            print(f"Error loading data for {symbol}: {e}")

    return dataframes, combined_df


# Example usage:
if __name__ == "__main__":
    BASE_PATH = "../data/yfinance_data/"
    STOCK_FILES = {
        "AAPL": "AAPL_historical_data.csv",
        "AMZN": "AMZN_historical_data.csv",
        "GOOG": "GOOG_historical_data.csv",
        "META": "META_historical_data.csv",
        "MSFT": "MSFT_historical_data.csv",
        "NVDA": "NVDA_historical_data.csv",
        "TSLA": "TSLA_historical_data.csv"
    }

    dataframes, combined_df = load_stock_data(BASE_PATH, STOCK_FILES)
    print("Combined DataFrame shape:", combined_df.shape)



def apply_technical_indicators(df):
    """
    Apply technical indicators (SMA, RSI, MACD) to a stock DataFrame.
    :param df: A DataFrame with stock data.
    :return: DataFrame with added technical indicators.
    """
    try:
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['SMA_200'] = df['Close'].rolling(window=200).mean()
        df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
        df['MACD'], df['MACD_signal'], _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        print("Applied technical indicators.")
    except Exception as e:
        print(f"Error applying indicators: {e}")
    return df


def calculate_sharpe_ratio(df):
    """
    Calculate the Sharpe Ratio for a stock.
    :param df: A DataFrame with stock data and 'Close' price.
    :return: Sharpe ratio value.
    """
    try:
        df['Daily_Return'] = df['Close'].pct_change()
        mean_return = df['Daily_Return'].mean()
        std_return = df['Daily_Return'].std()
        sharpe_ratio = mean_return / std_return * np.sqrt(252)  # Annualized
        print("Calculated Sharpe ratio.")
        return sharpe_ratio
    except Exception as e:
        print(f"Error calculating Sharpe ratio: {e}")
        return None
    


def plot_stock_indicators(df, symbol):
    """
    Plot stock price with technical indicators.
    :param df: A DataFrame with stock data and indicators.
    :param symbol: Stock symbol for labeling.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA', color='orange')
    plt.plot(df['Date'], df['SMA_200'], label='200-Day SMA', color='red')
    plt.title(f"{symbol} - Stock Price with Indicators")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()



