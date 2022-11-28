import requests
import json
response=request.get(https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest)

print(response.json()['init']) 