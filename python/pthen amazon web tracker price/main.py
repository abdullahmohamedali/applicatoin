import requests
from bs4 import BeautifulSoup
import  lxml
import re
html_of_website = requests.get("https://www.amazon.eg/-/en/Lenovo-Legion-16IRH8-13th-Intel-i7-13700H/dp/B0CQ7CW354/ref=sr_1_1?crid=U5EX1LZGPV5G")
html_only = html_of_website.text

soup = BeautifulSoup(html_only,"html.parser")

price_of_laptop = soup.find(class_ = "a-offscreen").text


html_of_website1 = requests.get("https://www.elgallagold.com/gold-coin-8")
html_only1 = html_of_website1.text


soup1 = BeautifulSoup(html_only1,"lxml")

h = soup1.find(class_ = "price-detail mb-0")

c = h.find(name = "strong").text

price_of_gold_coin = c.replace("Total: ", "")

numbers = re.findall(r"\d+,\d+|\d+\.\d+|\d+", price_of_gold_coin[4:])
numbers1 = re.findall(r"\d+,\d+|\d+\.\d+|\d+", price_of_laptop[3:])

cleaned_gold = float(numbers[0].replace(",", ""))  #
cleaned_laptop = float(numbers1[0].replace(",", ""))  #

print(f"the laptop needs you to {round(int(cleaned_laptop) / int(cleaned_gold),2)} pounds 😎 ")
