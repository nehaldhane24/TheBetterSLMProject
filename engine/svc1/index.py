import requests
import json

url = "https://api-supplychain.cisco.com/pdafapp/profiles_buglist_global_users/2.0/getProfileBugsListGU"
token ="abc" # add your token

payload = json.dumps({
  "contractId": "5862",
  "custName": "S&P GLOBAL",
  "profileName": "ISR 4K ASR 1K 17.6.3",
  "deliverables": "SARS",
  "limit": 100
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {token}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
