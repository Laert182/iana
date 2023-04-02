import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dados de exemplo
data = pd.DataFrame({'texto': ['Olá, tudo bem?', 'Qual é o seu nome?', 'O que você faz?', 'Quanto tempo vai levar?'],
                     'classe': ['saudação', 'identificação', 'função', 'tempo']})

# Preparação dos dados
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['texto'])
y = data['classe']

# Treinamento do modelo
clf = MultinomialNB()
clf.fit(X, y)

# Teste do modelo
novo_texto = 'Quanto tempo demora para entregar o pedido?'
novo_texto_transformado = vectorizer.transform([novo_texto])
predicao = clf.predict(novo_texto_transformado)
print(predicao)  # Saída: ['tempo']
