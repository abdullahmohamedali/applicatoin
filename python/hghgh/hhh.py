import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# JSON data (combined as shown above)
data = {
    "entière": "whole, entire",
    "mâcher": "to chew",
    "Ils": "They",
    "Ensuite": "Then, afterward",
    "tracer": "to draw, to trace",
    "crayon de couleur": "colored pencil",
    "chef-d’œuvre": "masterpiece",
    "répondu": "answered, responded",
    "Pourquoi": "Why",
    "chapeau": "hat",
    "intérieur": "inside, interior",
    "digérait": "was digesting",
    "comprendre": "to understand",
    "besoin": "need",
    "laisser de côté": "to leave aside, to set aside",
    "plutôt": "rather, instead",
    "abandonner": "to abandon, to give up",
    "carrière": "career",
    "devin": "soothsayer, fortune-teller",
    "devoir": "duty, obligation",
    "app": "app (abbreviation for application)",
    "avion": "airplane",
    "géographie": "geography",
    "servi": "served",
    "coup d'œil": "glance, a quick look",
    "égaré": "lost, misled",
    "cours": "course, during",
    "tas": "lots, heaps",
    "peints": "painted",
    "sérieux": "serious",
    "près": "near, close",
    "opinion": "opinion",
    "lucide": "lucid, clear-minded",
    "expérience": "experience",
    "conservé": "preserved, kept",
    "répondit": "responded",
    "portée": "reach, scope, range",
    "raisonnable": "reasonable"
}

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("Your Google Sheet Name").sheet1

# Insert headers
sheet.append_row(["French", "English"])

# Upload data to Google Sheets
for key, value in data.items():
    sheet.append_row([key, value])
