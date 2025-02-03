import pandas as pd
import matplotlib.pyplot as plt
from carregar_dados import df

airline_sentiment = df.groupby(["airline", "airline_sentiment"]).size().unstack()
airline_sentiment.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="coolwarm")
plt.xlabel("Companhia Aérea")
plt.ylabel("Número de Tweets")
plt.title("Distribuição de Sentimentos por Companhia Aérea")
plt.legend(title="Sentimento")
plt.savefig("../outputs/airline_sentiment.png")
plt.show()