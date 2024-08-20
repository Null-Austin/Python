import requests
#Whats the url again? Oh wait...
url = 'https://gasprices.aaa.com/state-gas-price-averages/'

#Real or Fake Browser? To be or Not to be...
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)

#lets fix them html
html=str(response.content).rstrip()
before=str(html.split('<p class="numb">',1)[1])
after=before.index('<i class="fa fa-caret-down" aria-hidden="true"></i>')
gasPrices=before[:after]
gasPrices=gasPrices[2:]
gasPrices=gasPrices.replace(" ","")

#pure beauty
print("\nThe Average Gas Price is: "+ gasPrices)

#extra code:
if float(gasPrices[1:])>=float(5):
    print("\nGet a better job")