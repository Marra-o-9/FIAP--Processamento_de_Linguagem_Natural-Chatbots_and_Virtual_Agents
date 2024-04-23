import spacy
from collections import Counter
from heapq import nlargest

# Carregando o modelo de idioma em português
nlp = spacy.load("pt_core_news_sm")

def summarize(text, num_sentences=2):
    # Tokenização do texto em sentenças
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    # Contagem de frequência das palavras
    word_freq = Counter()
    for word in doc:
        if not word.is_stop:
            word_freq[word.text.lower()] += 1

    # Cálculo da pontuação de cada sentença
    sent_scores = {}
    for sent in doc.sents:
        sentence_text = sent.text  # Obtenha o texto da sentença
        for word in sent:
            if word.text.lower() in word_freq:
                sent_scores[sentence_text] = sent_scores.get(sentence_text, 0) + word_freq[word.text.lower()]

    # Selecionando as melhores sentenças com base nas pontuações
    top_sentences = nlargest(num_sentences, sent_scores, key=sent_scores.get)

    # Juntando as sentenças selecionadas para formar o resumo
    summary = ' '.join(top_sentences)
    return summary

# Exemplo de uso
texto = """
Quando bebê, Harry Potter fora deixado na porta de seus tios maternos Petúnia Dursley (irmã mais velha de Lílian) e Válter Dursley. Harry cresceu na casa dos seus tios, que escondiam a verdade sobre sua família. Ao completar onze anos, o garoto começa a receber cartas de um remetente desconhecido, que aumentam de quantidade à medida que seus tios as destroem. Quando finalmente consegue abrir uma delas, Harry descobre que possui poderes mágicos, como os seus pais, e que foi aceito na Escola de Magia e Bruxaria de Hogwarts.

Em seguida, é revelado que os Potter não morreram num acidente de carro, como sempre dito a Harry, mas que foram assassinados por Lorde Voldemort, um dos maiores bruxos das trevas da história. Na noite do suposto acidente, Voldemort matou James e Lílian Potter, porém, ao tentar matar Harry, perdeu sua forma física e deixou uma cicatriz em forma de raio na testa do bebê.
"""

# Tokenizar o texto
documento = nlp(texto)

# Exibir tokens
for token in documento:
    print(token.text)

# Exibir informações morfológicas para cada token
for token in documento:
    print(f"Token: {token.text}, Forma básica: {token.lemma_}, Classe gramatical: {token.pos_}, Tag de detalhes: {token.tag_}")

# Exibir as entidades nomeadas encontradas
for entidade in documento.ents:
    print(f"Entidade: {entidade.text}, Tipo: {entidade.label_}")

summary = summarize(texto)
print(summary)
