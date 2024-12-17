

import os
import pandas as pd
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to format date for alignment
def format_date(date):
    return date.strftime('%Y-%m-%d')

# Function to perform sentiment analysis
def sentiment_analysis(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)

# Function to load and prepare the news data
def load_news_data(news_data_path):
    news_df = pd.read_csv(news_data_path, index_col=False)
    news_df = news_df.drop(columns=['Unnamed: 0'])
    news_df['date'] = pd.to_datetime(news_df['date'], utc=True, format="mixed")
    news_df['date'] = news_df['date'].apply(format_date)
    news_df['sentiment_score'] = news_df['headline'].apply(sentiment_analysis)
    return news_df

# Function to load and prepare the stock data
def load_stock_data(stock_data_paths, tickers):
    combined_df = pd.DataFrame()
    for ticker, stock_data_path in zip(tickers, stock_data_paths):
        stock_df = pd.read_csv(stock_data_path)
        stock_df['Symbol'] = ticker
        stock_df['date'] = pd.to_datetime(stock_df['Date'])
        stock_df['date'] = stock_df['date'].apply(format_date)
        stock_df = stock_df.sort_values(by="date", ascending=True)
        combined_df = pd.concat([combined_df, stock_df])
    combined_df['daily_return'] = combined_df.groupby('Symbol')['Close'].pct_change() * 100
    return combined_df

# Function to merge news and stock data
def merge_data(stock_df, news_df):
    merged_df = pd.merge(stock_df, news_df[['date', 'sentiment_score']], on='date', how='inner')
    return merged_df

# Function to perform correlation analysis
def correlation_analysis(merged_df):
    correlation = merged_df[['daily_return', 'sentiment_score']].corr()
    return correlation

# Function to visualize the correlation matrix
def plot_correlation(correlation):
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation between Stock Returns and News Sentiment')
    plt.show()

# Function to save merged data to CSV
def save_merged_data(merged_df, output_path):
    merged_df.to_csv(output_path, index=False)
