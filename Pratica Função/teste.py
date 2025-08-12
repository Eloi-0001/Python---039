def comida(Comida:str):
    if Comida == "Cenoura":
        print("vegetal")
    elif Comida == "Bife":
        print("Carne")
    elif Comida == "Laranja":
        print("Fruta")
    else:
        print("sei nao rei")

comida(input("qual comida?"))