import matplotlib.pyplot as plt
import seaborn as sns
def analyze_top_publishers(df):
    """Visualize contributions of top publishers."""
    publisher_counts = df['publisher'].value_counts()
    top_publishers = publisher_counts.head(10)

    top_publishers.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), colors=sns.color_palette("pastel"))
    plt.title("Top 10 Publishers Contribution")
    plt.ylabel("")
    plt.show()

def analyze_email_domains(df):
    """Analyze email domains of publishers."""
    df['email_domain'] = df['publisher'].str.extract(r'@([\w\.-]+)')
    domain_counts = df['email_domain'].value_counts()

    domain_counts.head(10).plot(kind='barh', color='orange')
    plt.title("Top 10 Email Domains by Frequency")
    plt.xlabel("Number of Articles")
    plt.ylabel("Email Domain")
    plt.show()
