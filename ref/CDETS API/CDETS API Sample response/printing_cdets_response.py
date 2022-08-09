import os
import sys
import re
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl import load_workbook
from openpyxl.worksheet.dimensions import ColumnDimension
from openpyxl.styles.alignment import Alignment
import time
import requests
import xmltodict
from requests_oauthlib import OAuth1
import json
import pprint

bug="CSCvy17498"

url = "https://cdetsng.cisco.com/wsapi/latest/api/bug/" + bug.rstrip() + "/fields"
auth_cred = OAuth1("5997c727-f57b-436c-9a2f-5934d52265b6", client_secret = "U5KOMwZx3uplrzfPAWhDi5UctdKfvcE0")
print(auth_cred)
response = requests.get(url, auth = auth_cred)
text=xmltodict.parse(response.text) #Convert the xml text to dict

