n = int(input("Factorielle de: "))
fn = 1

# i prend les valeurs les entiers de 0 à n - 1
for i in range(n):
    # (i + 1) prend pour valeurs de les entiers de 1 à n
    fn *= (i + 1)

# On affiche
print(fn)
