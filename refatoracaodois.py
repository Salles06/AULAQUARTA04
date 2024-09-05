idade = int(input ("começo de idade:"))

def verificarCategoriaIdade (numero):
    if idade < 13:
        return  "criança"
    elif idade >= 13 and idade < 18:
        return  "Adolescente"
    else:
        return  "adulto"

print(verificarCategoriaIdade (idade))