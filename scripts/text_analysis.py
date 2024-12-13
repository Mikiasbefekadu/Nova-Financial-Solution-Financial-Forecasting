
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer


def perform_sentiment_analysis(df):
    """Perform sentiment analysis on headlines."""
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['sentiment_category'] = pd.cut(
        df['sentiment'], bins=[-1, -0.05, 0.05, 1], labels=['negative', 'neutral', 'positive']
    )

    sentiment_counts = df['sentiment_category'].value_counts()
    sentiment_counts.plot(kind='bar', color=['red', 'grey', 'green'])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Articles")
    plt.show()

def generate_wordcloud(df):
    """Generate a word cloud for headlines."""
    text = " ".join(headline for headline in df['headline'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Headlines")
    plt.show()

def extract_keywords(df):
    """Extract common keywords using CountVectorizer."""
    vectorizer = CountVectorizer(stop_words='english', max_features=20)
    word_matrix = vectorizer.fit_transform(df['headline'])
    common_words = vectorizer.get_feature_names_out()
    print("Top 20 Keywords:", common_words)
