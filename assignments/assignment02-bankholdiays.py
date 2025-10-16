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




# tricky part where we check on unique date for northern Ireland

uk_bank_holidays_dates = []
for region in data:
    if region != 'northern-ireland':
        for event in data[region]['events']:
            if event['date'] not in uk_bank_holidays_dates:   
                uk_bank_holidays_dates.append(event['date'])

print("Other UK bank holiday dates:", uk_bank_holidays_dates)


unique_bank_holidays_ie = []
for event in data['northern-ireland']['events']:
    date = event['date']
    if date not in uk_bank_holidays_dates:
        unique_bank_holidays_ie.append(date)

print("Unique Northern Ireland bank holiday dates:", unique_bank_holidays_ie)
