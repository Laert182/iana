from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Baixa os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Define as etapas de pré-processamento
def preprocess_text(text):
    # Tokenização
    tokens = word_tokenize(text)
    
    # Remoção de pontuação e caracteres especiais
    table = str.maketrans('', '', string.punctuation)
    tokens = [t.translate(table) for t in tokens]
    
    # Remoção de stop words
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if not t.lower() in stop_words]
    
    # Lematização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    
    # Reunir tokens em uma string novamente
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

@app.route('/', methods=['POST'])
def preprocess():
    # Recebe o texto enviado pelo front-end
    text = request.form['text']
    
    # Pré-processa o texto
    preprocessed_text = preprocess_text(text)
    
    # Retorna o texto pré-processado para o front-end
    return jsonify({'preprocessed_text': preprocessed_text})

if __name__ == '__main__':
    app.run(debug=True)
