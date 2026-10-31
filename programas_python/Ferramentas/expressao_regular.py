"""

"""

import re #regular expression

cpf = '746.824.890-70'
cpf = re.sub(r'[^0-9]', '', cpf) #pega qualquer coisa que não for um número([^0-9]) e substitui por ''.
print(cpf)