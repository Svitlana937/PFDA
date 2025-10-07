import requests

url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
print(response) # the response code is printed in the console
data = response.json()
print(data) # the data is printed in the console as a dictionary

print(data['northern-ireland']['events'][0])