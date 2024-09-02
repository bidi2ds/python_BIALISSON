class Componente:
    def __init__(self, nome, peso, custo):
        self.nome = nome
        self.peso = peso
        self.custo = custo

    def __repr__(self):
        return f"{self.nome}: Peso = {self.peso}, Custo = {self.custo}"

# Ordenação natural (por nome)
def ordenar_natural(componentes):
    return sorted(componentes, key=lambda c: c.nome)

# Ordenação customizada (por peso)
def ordenar_customizada(componentes):
    return sorted(componentes, key=lambda c: c.peso)


componentes = [
    Componente("Rodízio", 2.5, 20),
    Componente("Motor", 150, 5000),
    Componente("Bateria", 30, 150),
]

print("Ordenação Natural:")
for c in ordenar_natural(componentes):
    print(c)

print("\nOrdenação Customizada:")
for c in ordenar_customizada(componentes):
    print(c)
