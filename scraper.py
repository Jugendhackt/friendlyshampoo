import requests
from bs4 import BeautifulSoup
import json

alle_produkte = {}

#shampooraussucher
#Link DM shampoosuche
url = "https://product-search.services.dmtech.com/de/search/static?allCategories.id=110101&pageSize=15&sort=editorial_relevance&currentPage=3&type=search-static"

r = requests.get(url)
j = r.json() 

laenge_produktliste = len(j["products"])
i = 0
while i< laenge_produktliste:
    artikelnummer = j["products"][i]["gtin"]
    i = i+1
    alle_produkte[artikelnummer] = {}




#ingredientraussucher
def ingredientraussucher(artikelnummer):    
    url = f"https://products.dm.de/product/de/products/gtins/{artikelnummer}?view=details"
    r = requests.get(url)

    l = r.json()
    j = l[0]

    ingredients = j["details"]["descriptionGroup"]["nonFoodIngredientsDescription"]["text"]

    ingredients_list = ingredients.split(" | ")
    return ingredients_list

for artikelnummer in alle_produkte.keys():
    alle_produkte[artikelnummer]["ingredients"] = ingredientraussucher(artikelnummer)

#speichern in the datei


file = open("alle_produkte.json","w")
json.dump(alle_produkte,file,indent=4)
file.close()
