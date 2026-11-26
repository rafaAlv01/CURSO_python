# Controlando a quantidade de argumentos posicionais e nomeados em funções

# Positional-Only Parameters (/) e Keyword-Only Arguments (*)

# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)

# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.
#           se fizer: soma(1, b=2, c=3, nome='teste'), vai dar erro, pois antes da barra só pode ser argumentos posicionais.

# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/

# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
#           Tudo que vem antes do * é posicional, tudo que vem depois é nomeado.

# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')