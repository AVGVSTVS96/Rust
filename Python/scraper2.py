""" string
"""

import requests
from bs4 import BeautifulSoup

# URL to scrape
URL = "http://rr-calendar.nycbar.org:8213/AVSchedule.aspx?curdate=0"
response = requests.get(URL, timeout=10)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all the table rows
rows = soup.find_all("tr")

# Create an empty list to store the data
data = []

# Loop through each row and extract the data
for row in rows:
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

# Filter out the rows with no data
data = [row for row in data if row]

# Create a list to store the formatted data
formatted_data = []

# Loop through each row of data and format it
for row in data:
    event = {}
    event["Setup Time"] = ""
    event["Start Time"] = row[0]
    event["Location"] = row[1]
    event["Event Title/Menu"] = row[2]
    event["Actual Guests"] = ""
    event["End Time"] = row[3]
    event["Tear Down Time"] = ""
    formatted_data.append(event)

# Print the formatted data
for event in formatted_data:
    print(event)
