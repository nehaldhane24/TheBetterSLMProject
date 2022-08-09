# Generate OAuthToken

import requests
import json

url = "https://cloudsso.cisco.com/as/token.oauth2"

payload='grant_type=password&client_id=EurusClient&client_secret=EurusClient&scope=profile&username=ishaukat&password=OnFireDragon1000!'

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

access_token=json.loads(response.text)['access_token']

# Whether the bug(s) is applicable

import requests

url = "https://api-supplychain.cisco.com/pdafapp/common/1.0/getMPBugDetails"

params={
    'osType':'N',
    'release':'7.3(1)D1(1)',
    'prodFamily':'Cisco Nexus 7000 Series Switches',
    'limit':10
}
payload={}
headers = {
  'Authorization': 'Bearer G73tA8YTmdnyDJZlcPeKGQuMHSFf',
  'Cookie': '2e572c1106cef1a1a48bb7704ce98235=cfb11eee57da64e108546c83c1df13b3'
}

response = requests.request("GET", url, headers=headers, data=payload, params=params)

print(response.text)


# Get profile bug details.  

import requests
import json

url = "https://api-supplychain.cisco.com/pdafapp/profiles_buglist_global_users/2.0/getProfileBugsListGU"

payload = json.dumps({
  "contractId": "5862",
  "custName": "S&P GLOBAL",
  "profileName": "ISR 4K ASR 1K 17.6.3",
  "deliverables": "SARS",
  "limit": 10
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer G73tA8YTmdnyDJZlcPeKGQuMHSFf',
  'Cookie': '2e572c1106cef1a1a48bb7704ce98235=cfb11eee57da64e108546c83c1df13b3'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
