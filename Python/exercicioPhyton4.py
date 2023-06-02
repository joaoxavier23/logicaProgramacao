def dados_produto(produto,quantidade_produto,valor_unitario):
    return produto,valor_unitario,quantidade_produto*valor_unitario
Compra=dados_produto('Leite',10,3)
print(f"O produto {Compra[0]} custa {Compra[1]} reais, valor  total da compra: {Compra[2]} ")
