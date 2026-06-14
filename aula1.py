l1 = float(input())
l2 = float(input())
l3 = float(input())

triangulo = str

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 != l2 and l2 != l3:
        triangulo = "Escaleno"
    elif l1 == l2 and l1 == l3 and l2 == l3:
        triangulo = "Equilátero"
    else:
        triangulo = "Isósceles"
else:
    triangulo = "Não forma um triângulo"

print(triangulo)