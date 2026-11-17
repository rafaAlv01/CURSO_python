# copy, sorted, produtos.sort
# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import metodos_produtos
from dados import produtos #só foi possível fazer isso com o arquivo __init__ especificando em qual pacote e em qual método está produtos.
#Observe: Esse método pode ver o pacote dados, mas não sabe onde está produtos. Quando o Python entra no pacote ele vai direto pro __init__.py que complementa a localização de produtos.

novos_produtos = metodos_produtos.aumentar_preco(produtos, 1.1)
produtos_ordenados_por_nome = metodos_produtos.ordem_decrescente(novos_produtos)
produtos_ordenados_por_preco = metodos_produtos.ordem_preco_crescente(novos_produtos)

print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')