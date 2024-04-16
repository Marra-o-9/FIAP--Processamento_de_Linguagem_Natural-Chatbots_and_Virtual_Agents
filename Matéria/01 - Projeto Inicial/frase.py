
dicionario = {
    'boas': ["legal", "bom", "demais", "poggers"],
    'ruins': ["ruim", "cocô", "bosta", "noggers"],
}

dicionario_intensidade = {
    'aumenta_muito': ["muito", "pouco"],
    'aumenta_medio': ["bem"],
    'aumenta_pouco': ["mais", "menos"]
}

frase = input("Digite uma frase: ")
palavras = frase.split(" ")
positividade = 0
negatividade = 0

for palavra in palavras:
    for chave, valores in dicionario.items():
        if palavra.lower() in valores:
            if chave == 'boas':
                if (valores['aumenta_muito'] + " " + palavra) in frase:
                    positividade = (positividade + 1) * 3
                elif (valores['aumenta_medio'] + " " + palavra) in frase:
                    positividade = (positividade + 1) * 2
                elif (valores['aumenta_pouco'] + " " + palavra) in frase:
                    positividade = (positividade + 1) * 1.5
                else:
                    positividade += 1
            elif chave == 'ruins':
                if (valores['aumenta_muito'] + " " + palavra) in frase:
                    negatividade = (negatividade + 1) * 3
                elif (valores['aumenta_medio'] + " " + palavra) in frase:
                    negatividade = (negatividade + 1) * 2
                elif (valores['aumenta_pouco'] + " " + palavra) in frase:
                    negatividade = (negatividade + 1) * 1.5
                else:
                    negatividade += 1

print(positividade)
print(negatividade)
resultado = positividade - negatividade

if resultado > 0:
    print("Frase positiva.")
elif resultado < 0:
    print("Frase negativa.")
else:
    print("Frase neutra.")
