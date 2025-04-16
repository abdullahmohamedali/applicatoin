import requests
from bs4 import BeautifulSoup
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

html = requests.get("https://appbrewery.github.io/Zillow-Clone/").text


soup= BeautifulSoup(html,"html.parser")

prices = soup.find_all(name = "span", class_ = "PropertyCardWrapper__StyledPriceLine")

addresses = soup.find_all("address")

links = soup.find_all(name="a", class_="property-card-link")
prices_f_text = [
    re.sub(r"[^\d]", "", price.get_text(strip=True)) for price in prices
]  # Removes everything except numbers
link_f_herf = []
adr_f_text =[]
for adr in addresses:
    adr_f_text.append(adr.get_text(strip=True).replace("\n", "").replace(",", ""))
for link in links:
    link_f_herf.append(link.get("href"))


creds = ServiceAccountCredentials.from_json_keyfile_name("/home/abdullah/Documents/google_sheets/the-web-scrapping-automation-7422f5232462.json", ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("zillow scrapiing").sheet1  # Opens first sheet

for price, address, link in zip(prices_f_text, adr_f_text, link_f_herf):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
    sheet.append_row([timestamp, price, address, link])
    print(f"Added: {timestamp}, {price}, {address}, {link}")

print("✅ Data added to Google Sheets successfully!")









