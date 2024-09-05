#Variação Global
idade = int(input ("Qual a sua idade?"))

# No trecho de condição será validado a idade da persona para analisar sia categoria
def verificarCategoriaIdade (idade):
    if idade < 0:
        return  "Essa pessoa por acaso já nasceu?"
    elif idade > 0 and idade < 2:
        return  "Bebê"
    elif idade > 2 and idade < 13:
        return "Você é uma criança!"
    elif idade >= 13 and idade < 18:
        return "Você é um adolescente!"
    elif idade >= 18 and idade <=60:
        return "Você é um adulto!"
    elif idade > 60 and idade <= 105:
        return "Você é um idoso!"
    else:
        return " Alguem verifica se ainda esta vivo"

categoria = verificarCategoriaIdade(idade)
print(categoria)
