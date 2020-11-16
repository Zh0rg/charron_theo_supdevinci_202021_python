subject = ["I", "You"]
verbs = ["Play", "Love"]
complements = ["Hockey", "Football"]

for subject in subjects:
    # Pour chaque sujet, on boucle sur les verbes
    for verb in verbs:
        # Pour chaque verbe, on boucle sur les complements
        for complement in complements:
            print("{} {} {}".format(subject, verb, complement))
