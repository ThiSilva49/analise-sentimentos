# Análise de Sentimentos em Tweets sobre Companhias Aéreas

Este projeto realiza uma análise de sentimentos em tweets sobre companhias aéreas usando um dataset público. São geradas diversas visualizações para entender padrões e insights sobre os sentimentos expressos pelos usuários.

projeto-analise-sentimentos/ │ ├── 📂 data/ # Pasta para armazenar os datasets │ └── Tweets.csv # Dataset de tweets sobre companhias aéreas │ ├── 📂 scripts/ # Scripts Python para análise de dados │ ├── carregar_dados.py # Carrega o dataset e faz pré-processamento dos dados │ ├── distribuicao_sentimentos.py # Gera gráfico de distribuição de sentimentos │ ├── evolucao_sentimentos.py # Analisa a evolução dos sentimentos ao longo do tempo │ ├── nuvem_palavras.py # Cria uma nuvem de palavras para sentimentos negativos │ ├── analise_negativa.py # Analisa as razões para sentimentos negativos │ └── sentimento_por_companhia.py # Examina sentimentos por companhia aérea │ ├── 📂 outputs/ # Pasta para salvar imagens e resultados │ ├── sentiment_distribution.png # Gráfico de distribuição de sentimentos │ ├── sentiment_over_time.png # Gráfico da evolução dos sentimentos ao longo do tempo │ ├── wordcloud_negative.png # Nuvem de palavras dos sentimentos negativos │ ├── negative_reasons.png # Análise das razões para sentimentos negativos │ └── airline_sentiment.png # Sentimentos por companhia aérea │ └── README.md # Explicação do projeto e instruções


└── README.md                   # Explicação do projeto e instruções

📊 Visualizações Geradas

Distribuição de Sentimentos - Gráfico de barras mostrando o número de tweets positivos, negativos e neutros.

Evolução dos Sentimentos - Linha do tempo mostrando a variação dos sentimentos ao longo dos dias.

Nuvem de Palavras - Palavras mais frequentes nos tweets negativos.

Principais Razões para Sentimentos Negativos - Frequência das principais reclamações.

Sentimento por Companhia Aérea - Análise dos sentimentos associados a cada empresa.

🚀 Como Executar

Instale as dependências:

pip install -r requirements.txt

Execute os scripts na pasta scripts conforme necessário:

python scripts/distribuicao_sentimentos.py

📌 Requisitos

Python 3.x

Pandas

Matplotlib

Seaborn

WordCloud
