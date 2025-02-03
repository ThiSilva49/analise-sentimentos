import seaborn as sns
import matplotlib.pyplot as plt
from carregar_dados import df

neg_reasons = df["negativereason"].value_counts().dropna()
plt.figure(figsize=(10, 5))
sns.barplot(y=neg_reasons.index, x=neg_reasons.values, palette="Reds_r")
plt.xlabel("Número de Tweets")
plt.ylabel("Razão do Sentimento Negativo")
plt.title("Principais Razões para Sentimentos Negativos")
plt.savefig("../outputs/negative_reasons.png")
plt.show()