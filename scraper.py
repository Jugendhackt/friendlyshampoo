import requests
from bs4 import BeautifulSoup


#shampooraussucher

url = "https://product-search.services.dmtech.com/de/search/static?allCategories.id=110101&pageSize=15&sort=editorial_relevance&currentPage=3&type=search-static"
r = requests.get(url)


j = r.json() 


(len(j["products"]))
i = 0
while i< len(j["products"]):
    artikelnummer = j["products"][i]["gtin"]
    i = i+1




#ingredientraussucher
url = f"https://products.dm.de/product/de/products/gtins/{artikelnummer}?view=details"
r = requests.get(url)


l = r.json()
j = l[0]

ingredients = j["details"]["descriptionGroup"]["nonFoodIngredientsDescription"]["text"]

ingredients_list = ingredients.split(" | ")
print(ingredients_list)