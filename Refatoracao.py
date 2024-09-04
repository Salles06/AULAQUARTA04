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

