import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
def analyze_headline_length(df):
    """Analyze headline lengths and plot the distribution."""
    df['headline_length'] = df['headline'].apply(len)
    print(df['headline_length'].describe())

    sns.histplot(df['headline_length'], bins=30, kde=True, color='blue')
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()

def articles_per_publisher(df):
    """Count and visualize articles per publisher."""
    publisher_counts = df['publisher'].value_counts()
    print(publisher_counts.head(10))

    publisher_counts.head(10).plot(kind='barh', color='skyblue')
    plt.title("Top 10 Publishers by Number of Articles")
    plt.xlabel("Number of Articles")
    plt.ylabel("Publisher")
    plt.show()


def process_dates(df):
    """
    Processes the 'date' column in the DataFrame to extract hour, day, and month.
    Converts the 'date' column to datetime format if not already in datetime format.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing a 'date' column.
    
    Returns:
    pd.DataFrame: The DataFrame with new columns for hour, day, and month.
    """
    # Convert 'date' column to datetime (if not already done)
    df['date_conv'] = pd.to_datetime(df['date'], utc=True, format="mixed")
    
    # Extract hour, day, and month
    df['hour'] = df['date_conv'].dt.hour
    df['day'] = df['date_conv'].dt.day_name()
    df['month'] = df['date_conv'].dt.month_name()

    return df



def analyze_publication_dates(df):
    # Order of the months and days
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Convert the 'month' and 'day' columns to categorical types with a specific order
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    df['day'] = pd.Categorical(df['day'], categories=day_order, ordered=True)
    
    # Analyze articles published per day of the week
    articles_per_day = df['day'].value_counts().sort_index()
    print("Articles per day of the week:\n", articles_per_day)

    # Analyze articles published per month
    articles_per_month = df['month'].value_counts().sort_index()
    print("Articles per month:\n", articles_per_month)

    # Analyze articles published by hour
    articles_per_hour = df['hour'].value_counts(normalize=True).sort_index()
    print("Articles per hour (normalized):\n", articles_per_hour)

    # Plotting results

    
    plt.figure(figsize=(12, 8))

    # Plot articles per day
    plt.subplot(3, 1, 1)
    articles_per_day.plot(kind='bar', color='blue', title='Articles Published Per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Articles')

    # Plot articles per month
    plt.subplot(3, 1, 2)
    articles_per_month.plot(kind='bar', color='orange', title='Articles Published Per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')

    # Plot articles per hour
    plt.subplot(3, 1, 3)
    articles_per_hour.plot(kind='bar', color='green', title='Articles Published Per Hour (Normalized)')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Proportion of Articles')

    plt.tight_layout()  # Adjust subplots to fit in the figure area.
    plt.show()
