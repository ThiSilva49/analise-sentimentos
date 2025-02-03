from wordcloud import WordCloud
import matplotlib.pyplot as plt
from carregar_dados import df

negative_tweets = " ".join(df[df["airline_sentiment"] == "negative"]["text"])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(negative_tweets)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Nuvem de Palavras - Tweets Negativos")
plt.savefig("../outputs/wordcloud_negative.png")
plt.show()