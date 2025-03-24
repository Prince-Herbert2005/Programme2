a = int(input("Entrez le 1er N:"))
b = int(input("Entrez le 2em N:"))
op = input("Entrez operateur(+,-,*,/):")
if op == "+":
    print("a+b",a+b)
elif op == "-":
    print("a-b",a-b)
elif op == "*":
    print("a*b",a*b)
elif op == "/":
    if b != 0:
        print("a/b",a/b)
    else:
        print("impossible de diviser par 0")
else:
    print("operateur invalide")