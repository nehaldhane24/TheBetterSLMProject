import requests

url = "https://mimir-prod.cisco.com/api/mimir/sora/all_projects_with_engineer_details?limit=1"

payload={}
headers = {
  'Authorization': 'Bearer 0Pt4xeryx1LgycrwApvp1mVI763p',
  'Cookie': 'mimir=eyJleHBpcmF0aW9uIjoiNDMyMDAiLCJleHBpcmVzIjoxNjU4NzMzMDg2LCJ1c2VyaWQiOiJpc2hhdWthdCJ9--348759ddde35b5203eea959514d89a85d571db78'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
