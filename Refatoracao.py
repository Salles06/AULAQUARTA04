# variaveis SUM[]

valorProduto = [100, 200, 300]

# Soma dos Produtos

totalProdutos = sum(valorProduto)

print(totalProdutos)

# Criando o desconto

valorDesconto = 0

if totalProdutos > 500:
  valorDesconto = totalProdutos * 0.1

totalcomDesconto = totalProdutos - valorDesconto

# Resultado final

print(f"Valor com desconto é : {totalcomDesconto}" )

# Comparação

# Variaveis de Preço
p1 = 100
p2 = 200
p3 = 300

t = p1 + p2 + p3

desc = 0
if t > 500:
    desc = t * 0.1

r = t - desc

print("Total antes do desconto:", t)
print("Desconto aplcado:", desc)
print("Total com desconto:", r)