class Peça:
    def __init__(self, nome, peso, custo):
        self.nome = nome
        self.peso = peso
        self.custo = custo

    def __repr__(self):
        return f"{self.nome}: Peso = {self.peso}kg, Custo = R${self.custo}"

def ordenar_total(pecas):
    """Ordena a lista de peças com base em nome, peso e custo."""
    return sorted(pecas, key=lambda p: (p.nome, p.peso, p.custo))


pecas = [
    Peça("Filtro de Óleo", 0.5, 50),
    Peça("Alternador", 4.2, 300),
    Peça("Velas de Ignição", 0.1, 20),
    Peça("Radiador", 10.0, 200),
    Peça("Bateria", 12.5, 400)
]


pecas_ordenadas_total = ordenar_total(pecas)
print("Ordenação Total por Nome, Peso e Custo:")
for p in pecas_ordenadas_total:
    print(p)
class Peça:
    def __init__(self, nome, peso, custo):
        self.nome = nome
        self.peso = peso
        self.custo = custo

    def __repr__(self):
        return f"{self.nome}: Peso = {self.peso}kg, Custo = R${self.custo}"

def ordenar_total(pecas):
    """Ordena a lista de peças com base em nome, peso e custo."""
    return sorted(pecas, key=lambda p: (p.nome, p.peso, p.custo))


pecas = [
    Peça("Filtro de Óleo", 0.5, 50),
    Peça("Alternador", 4.2, 300),
    Peça("Velas de Ignição", 0.1, 20),
    Peça("Radiador", 10.0, 200),
    Peça("Bateria", 12.5, 400)
]


pecas_ordenadas_total = ordenar_total(pecas)
print("Ordenação Total por Nome, Peso e Custo:")
for p in pecas_ordenadas_total:
    print(p)
