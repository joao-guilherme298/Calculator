print("ola, bem vindo a calculadora de bhaskara!/n")
a = float(input("Digite o A: "))
b = float(input("Digite o B: "))
c = float(input("Digite o C: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Existe uma raiz real: {raiz}")
else:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    print(f"Existem duas raízes reais: {raiz1} e {raiz2}")

