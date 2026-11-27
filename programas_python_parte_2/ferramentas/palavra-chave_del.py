"""
    Em Python, a palavra-chave del remove uma referência (um nome de variável, um atributo de objeto, um item de lista ou uma chave de dicionário). Ela não apaga o objeto diretamente da memória — apenas desvincula aquele nome ou posição; o objeto só é destruído pelo Garbage Collector quando não sobrar nenhuma referência apontando para ele.
"""

class Carro:

    def __init__(self, nome):
        self.nome = nome


c1 = Carro("Fusca")

c1 = Carro("Gol")
c2 = c1  # Agora duas variáveis apontam para o mesmo objeto

del c1  # Remove apenas o nome 'c1'; o objeto continua vivo em 'c2'
print(c2.nome)  # 'Gol'

del c2  # Agora 0 referências restam -> Python libera a memória