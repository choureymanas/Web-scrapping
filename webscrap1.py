import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url="https://www.tarladalal.com/All-Recipes-308427c"


uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

container=page_soup.findAll("div",{"class":"rcc_recipecard"})
container1=container[0]
for container1 in container:
    container2=container1.findAll("span",{"class":"rcc_recipename"})
    container3=container2[0]
    container4=container3.a
    recipe_name=container4.text
    print(recipe_name+"\n")
