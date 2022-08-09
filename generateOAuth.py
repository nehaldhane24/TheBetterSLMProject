import requests

url = "https://cloudsso.cisco.com/as/token.oauth2"

username='cecID' # Enter you CEC ID
password='xyz' # Enter your password

payload='''grant_type=password&client_id=EurusClient&client_secret=EurusClient&scope=profile&username={username}&password={password}!'''
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
