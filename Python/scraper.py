"""This module contains a script for scraping the in-person calendar web page and
converting the data to JSON format."""

import json
import requests
from bs4 import BeautifulSoup

# Send a request to the web page
URL = "http://rr-calendar.nycbar.org:8213/AVSchedule.aspx?curdate=0"
response = requests.get(URL, timeout=10)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the form element that contains the event data
form = soup.find('form')

# Extract the event data from the form element
events = []
for event in form.find_all('tr'):
    event_data = {}
    for i, td in enumerate(event.find_all('td')):
        if i == 0:
            event_data['Subject'] = td.text
        elif i == 1:
            event_data['Start'] = td.text
        elif i == 2:
            event_data['End'] = td.text
    events.append(event_data)

# Convert the event data to JSON format
inperson_calendar = json.dumps(events)
print(events)
