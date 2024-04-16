dicionario = {
    'boas': ["legal", "bom", "demais", "poggers", "excelente", "ótimo", "incrível", "fantástico", "maravilhoso",
             "fenomenal", "espetacular", "sensacional", "notável", "extraordinário", "impressionante", "estupendo",
             "formidável", "surrupiado", "esplêndido", "radiante", "incomparável", "excepcional", "especial", 
             "gratificante", "triunfante", "perfeito", "divino", "fabuloso", "celestial",
             "supremo", "magistral", "inigualável", "lendário", "majestoso", "deslumbrante", "suntuoso",
             "glorioso", "fenomenal", "deslumbrante", "sublime", "deslumbrante"],
    'ruins': ["ruim", "cocô", "bosta", "merda", "noggers", "terrível", "horrível", "desastroso", "abominável",
              "deplorável", "lamentável", "péssimo", "execrável", "detestável", "repugnante", "medonho",
              "macabro", "malévolo", "sinistro", "nefasto", "maldito", "diabólico", "demoníaco", "miserável", "desgraçado",
              "desesperador", "aberrante", "assustador", "terrífico", "horripilante", "repulsivo", "horrendo",
              "indesejável", "nojento", "desagradável", "insuportável", "repelente", "insuportável", "indigno", "vulgar",
              "infeliz", "desgraçado", "infortunado", "desprezível", "inaceitável", "desumano", "abjeto", "repugnante"],
    'aumenta_muito': ["muito", "tão"],
    'aumenta_medio': ["bem"],
    'aumenta_pouco': ["mais"]
}

 
frase = input("Digite uma frase para analisar sua positividade: ")
palavras = frase.split(" ")
positividade = 0
negatividade = 0
 
for indice, palavra in enumerate(palavras):
    for chave, valores in dicionario.items():
        if palavra.lower() in valores:
            if chave == 'boas':
                if palavras[indice - 1] in dicionario['aumenta_muito']:
                    positividade = (positividade + 1) * 3
                elif palavras[indice - 1] in dicionario['aumenta_medio']:
                    positividade = (positividade + 1) * 2
                elif palavras[indice - 1] in dicionario['aumenta_pouco']:
                    positividade = (positividade + 1) * 1.5
                else:
                    positividade += 1
            elif chave == 'ruins':
                if palavras[indice - 1] in dicionario['aumenta_muito']:
                    negatividade = (negatividade + 1) * 3
                elif palavras[indice - 1] in dicionario['aumenta_medio']:
                    negatividade = (negatividade + 1) * 2
                elif palavras[indice - 1] in dicionario['aumenta_pouco']:
                    negatividade = (negatividade + 1) * 1.5
                else:
                    negatividade += 1
 
 
print(positividade)
print(negatividade)
resultado = positividade - negatividade

if resultado >= 3:
    print("No geral, é uma frase muito positiva.")
elif resultado >= 2:
    print("No geral, é uma frase bem positiva.")
elif resultado >= 1:
    print("No geral, é uma frase positiva.")
elif resultado <= -3:
    print("No geral, é uma frase muito negativa.")
elif resultado <= -2:
    print("No geral, é uma frase bem negativa.")
elif resultado <= -1:
    print("No geral, é uma frase negativa.")
else:
    print("No geral, é uma frase neutra.")