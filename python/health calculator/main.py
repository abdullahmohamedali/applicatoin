import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime

exercise = input("Enter the type of exercise: ")
duration = input("Enter the duration in minutes: ")

# Convert duration to an integer
duration = int(duration)

today = datetime.today().strftime('%Y-%m-%d')
# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
import requests


# Convert the duration to an integer
duration = int(duration)
# Your Nutritionix API credentials
APP_ID = '5a332749'
API_KEY = '38837fd58f28cf3a54dfd2fc271c5508'  # Replace with your actual API_KEY

def get_calories_burned(exercise, duration):
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "query": f"{exercise} for {duration} minutes"
    }

    # Send the POST request to Nutritionix
    response = requests.post(url, headers=headers, json=data)
    
    # Convert the response to JSON format
    result = response.json()
    
    if response.status_code == 200:
        # Access the calories burned from the response
        calories_burned = result["exercises"][0]["nf_calories"]
        return calories_burned
    else:
        # Handle errors
        print("Error:", result)
        return None

# Example usage
exercise = "running"
duration = 30  # in minutes
calories_burned = get_calories_burned(exercise, duration)


creds = ServiceAccountCredentials.from_json_keyfile_name('workout-433907-7567ff56c532.json', scope)
client = gspread.authorize(creds)

# Open a sheet from the spreadsheet
sheet = client.open("workout").sheet1  # Replace with your sheet name



# Append the data as a new row
sheet.append_row([today,exercise, duration, calories_burned])

print("Data saved successfully!")

# Example: Get all values in the sheet
data = sheet.get_all_records()