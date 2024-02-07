import requests
import os,json

response=requests.get('https://api.chucknorris.io/jokes/random')
print(response)
#200=Success
#300=Redirect
#400=Error
#404=Not foundable
data=[]
for i in range(11):
    response=requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code==200:
        data.append(response.json())
        

