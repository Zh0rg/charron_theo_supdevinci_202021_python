def multiple7(n):
    # i prend pour valeurs les entiets de 0 à n
    for i in range(n + 1):
        # Si i est divisible par 7
        if i % 7 == 0:
            yield i

def multiple7_alternative(n):
    # i prend pour valeurs les entiers multiples de 7 entre 0 et n
    for i in range(0, n + 1, 7):
        yield i

# Test
n = int(input("Générer jusqu'à: "))

# multiple7 ne renvoie que les nombres multiples de 7 entre 0 et n
for i in multiple7(n):
    print(i)
