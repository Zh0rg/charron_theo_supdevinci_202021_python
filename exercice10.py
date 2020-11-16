sujets = ["I", "You"]
verbes = ["Play", "Love"]
complements = ["Hockey", "Football"]

for sujet in sujets:
    # Pour chaque sujet, on boucle sur les verbes
    for verbe in verbes:
        # Pour chaque verbe, on boucle sur les complements
        for complement in complements:
            print("{} {} {}".format(sujet, verbe, complement))
