parsed = None

# Le module requests n'est pas présent nativement dans python
# Il faut l'installer avec la commande pip install requests
try:
    # Pour faire des requêtes
    import requests

    # Pour obtenir le contenu de l'URL spécifiée au format JSON
    parsed = requests.get("https://restcountries.eu/rest/v2/region/europe").json()
except ModuleNotFoundError:
    # Pour parser le JSON
    import json
    # Pour faire la requête et obtenir le fichier
    import urllib.request

    # Permet d'obtenir le contenu de l'URL spécifiée
    file = urllib.request.urlopen("https://restcountries.eu/rest/v2/region/europe").read()
    # Parse fichier et renvoie une liste ou un dictionnaire
    parsed = json.loads(file)

# Pour chaque item de la liste contenue dans parsed
for item in parsed:
    # Pour chaque item, on affiche le nom et le nombre d'habitants
    print(item['name'] + ': ' + str(item['population']) + ' habitants')
