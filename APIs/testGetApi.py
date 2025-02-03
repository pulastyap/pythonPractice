import requests
import pandas as pd

response = requests.get("https://api.data.gov.in/resource/f17a1608-5f10-4610-bb50-a63c80d83974?api-key=579b464db66ec23bdd0000012873375c637042ba6ed8d3d944375c13&format=json&filters%5BstateNameEnglish.keyword%5D=Bihar")

response_json = response.json()
print(response_json['records'])
# print('Title:', response_json['title'])
# print('Sector:', response_json['sector'])
# print('Records:', response_json['records'])

print(pd.DataFrame(response_json['records']))