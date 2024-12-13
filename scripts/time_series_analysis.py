import matplotlib.pyplot as plt
import pandas as pd 

def analyze_publication_frequency(df):
    """Analyze daily publication frequency."""
    df.set_index('date_conv', inplace=True)
    df['publication_count'] = 1
    daily_articles = df['publication_count'].resample('D').sum()

    daily_articles.plot(figsize=(12, 6), color='purple')
    plt.title("Daily Article Publication Frequency")
    plt.xlabel("date_conv")
    plt.ylabel("Number of Articles")
    plt.show()

def analyze_publishing_times(df):
    """Analyze publication times by hour."""
    # Ensure that the index is a DatetimeIndex
    df.index = pd.to_datetime(df.index, errors='coerce')  # Coerce invalid parsing to NaT (Not a Time)
    
    # Extract the hour from the datetime index
    df['hour'] = df.index.hour
    
    # Count articles published per hour
    hourly_articles = df['hour'].value_counts().sort_index()

    # Plot the result
    hourly_articles.plot(kind='bar', color='orange')
    plt.title('Articles Published Per Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Articles')
    plt.show()

