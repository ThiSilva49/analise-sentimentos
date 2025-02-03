import pandas as pd
import matplotlib.pyplot as plt
from carregar_dados import df

df["tweet_created"] = pd.to_datetime(df["tweet_created"])
df["date"] = df["tweet_created"].dt.date
sentiment_over_time = df.groupby(["date", "airline_sentiment"]).size().unstack()
sentiment_over_time.plot(figsize=(10, 6), marker='o')
plt.xlabel("Data")
plt.ylabel("Número de Tweets")
plt.title("Evolução dos Sentimentos ao Longo do Tempo")
plt.legend(title="Sentimento")
plt.savefig("../outputs/sentiment_over_time.png")
plt.show()