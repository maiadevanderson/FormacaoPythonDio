# Lê as três palavras
x = input()
y = input()
z = input()

# Verifica as combinações para determinar o animal
if x == "vertebrado":
    if y == "ave":
        if z == "carnivoro":
            animal = "aguia"
        elif z == "onivoro":
            animal = "pomba"
    elif y == "mamifero":
        if z == "onivoro":
            animal = "homem"
        elif z == "herbivoro":
            animal = "vaca"
elif x == "invertebrado":
    if y == "inseto":
        if z == "hematofago":
            animal = "pulga"
        elif z == "herbivoro":
            animal = "lagarta"
    elif y == "anelideo":
        if z == "hematofago":
            animal = "sanguessuga"
        elif z == "onivoro":
            animal = "minhoca"

# Imprime o nome do animal correspondente
print(f"{animal}")
