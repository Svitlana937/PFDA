# The program print out the dates of the bank holidays that happen in northern Ireland.
# Author: Svetlana Kozlovska

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

bank_holidays_dates = []

for event in data['northern-ireland']['events']:
    if 'bank' in event['title'].lower():
        bank_holidays_dates.append(event['date'])

print(bank_holidays_dates)