import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.bonappetit.com/recipe/banana-bread'

#opening up connection, then grabbing the page
uClient = uReq(my_url) #error here
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

title_container = page_soup.find("div", {"class":"max-width-container"})
recipe_title = title_container.h1.text

serving_container = page_soup.find("div", {"class": "post-dek-meta"})
serving_size = serving_container.span.text

ingredient_containers = page_soup.findAll("li", {"class" : "ingredient"})

ingredient_arr = []

for ingredient in ingredient_containers:
	ingredient_arr.append(ingredient.text)

print(recipe_title)	
print(serving_size)
print(ingredient_arr)