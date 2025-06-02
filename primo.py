numero = int(input("Ingrese un número: "))

divisores = []

print(f"Verificando divisores de {numero}:")

for i in range(2, numero + 1):  
    divisor = i
    resultado = numero / divisor
    if numero % divisor == 0:
        divisores.append(divisor)
        print(f"{numero} ÷ {divisor} = {resultado} (División exacta)")
    else:
        print(f"{numero} ÷ {divisor} = {resultado:.2f} (Con residuo)")

print(f"\nDivisores encontrados: {divisores}")

if len(divisores) == 2:
    print(f"{numero} ES PRIMO")
else:
    print(f"{numero} NO ES PRIMO")