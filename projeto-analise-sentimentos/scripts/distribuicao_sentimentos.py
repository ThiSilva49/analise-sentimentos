import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np

dataset_path = "Tweets.csv"
df = pd.read_csv(dataset_path)
sns.set_style("whitegrid")
sentiment_counts = df["airline_sentiment"].value_counts()
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=["red", "gray", "green"])
plt.xlabel("Sentimento")
plt.ylabel("Número de Tweets")
plt.title("Distribuição de Sentimentos nos Tweets")
plt.savefig("sentiment_distribution.png")
plt.show()