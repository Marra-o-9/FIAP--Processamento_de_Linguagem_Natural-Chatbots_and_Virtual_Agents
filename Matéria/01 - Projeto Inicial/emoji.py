dicionario = {
    'boas': ["❤", "😂", "👍", "😎"],
    'ruins': ["😭", "🤮", "😡", "💀"]
}


frase = input("Digite uma frase com emojis: ")

# Problema com split se não for dado o espaço no input
palavras = frase.split(" ")
positividade = 0

for palavra in palavras:
    for chave, valores in dicionario.items():
        if palavra.lower() in valores:
            if chave == 'boas':
                positividade += 1
            elif chave == 'ruins':
                positividade -= 1

if positividade > 0:
    print("Frase com emoji(s) positivo(s).")
elif positividade < 0:
    print("Frase com emoji(s) negativo(s).")
else:
    print("Frase neutra.")
