import sys
import argparse
import requests
import xmltodict
from requests_oauthlib import OAuth1


def call_cdets_api(bug):
    url = "https://cdetsng.cisco.com/wsapi/latest/api/bug/" + bug.rstrip() + "/fields"
    auth_cred = OAuth1("5997c727-f57b-436c-9a2f-5934d52265b6", client_secret = "U5KOMwZx3uplrzfPAWhDi5UctdKfvcE0")
    response = requests.get(url, auth = auth_cred)
    #Convert the xml text to dict
    return xmltodict.parse(response.text)	

def find_field(cdets_bug_info, field):
    #Search for Component Field in CDETS JSON response
    for val in cdets_bug_info["CDETS"]["Defect"]["Field"]:
        if val['@name'] == field:		
            return val['#text']
            #slm_ws.cell(row = bug_row, column = 6, value = val['#text'])
    return None

def Workaround_Availability_Process(cdets_bug_info):
    workaround_data=find_field(cdets_bug_info,"Workarounds")
    if workaround_data==None:
        return 'N'
    if len(workaround_data.split())>5:
        return 'Y'
    else:
        return 'N'

def RNE_Process(cdets_bug_info):
    RNE = []
    for val in cdets_bug_info["CDETS"]["Defect"]["Field"]:										
        if val['@name'] == "Symptoms":	
            RNE.extend(['Symptom:',val['#text']])
    for val in cdets_bug_info["CDETS"]["Defect"]["Field"]:
        if val['@name'] == "Conditions":	
            RNE.extend(['Condition:',val['#text']])
    if(Workaround_Availability_Process(cdets_bug_info)=='Y'):
        RNE.extend(["No workarond available"])
    for val in cdets_bug_info["CDETS"]["Defect"]["Field"]:
        if val['@name'] == "Workarounds":	
            RNE.extend(['Workaround:',val['#text']])
    for val in cdets_bug_info["CDETS"]["Defect"]["Field"]:
        if val['@name'] == "Further-Problem-Description":	
            RNE.extend(['Further Problem Description:',val['#text']])
    if len(RNE)!=0:
        return '\n'.join(RNE)
    return None

if __name__== '__main__':

    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--bug', '-b', type=str, help="Enter Bug Name")
    args = my_parser.parse_args()

    if args.bug is  None:
        print("The following arguments are required: --bug/-b\nPlease pass the bug name as an argument\nUsage: cdetsAPI.py [-h] --bug BUG")
        exit()

    bug=args.bug
    cdets_bug_info=call_cdets_api(bug)

    print("Summary on Bug",bug,":")
    rne=RNE_Process(cdets_bug_info)
    print("Notes:","---------",rne,sep="\n")

    print()

    component=find_field(cdets_bug_info,"Component")
    print("Component:","---------",component,sep="\n")

    print()

    found=find_field(cdets_bug_info,"Found-during")
    originally_found=find_field(cdets_bug_info,"Original-found")
    print("Found During:","---------",found,"\nOriginally found during:","---------",originally_found,sep="\n")

    print()