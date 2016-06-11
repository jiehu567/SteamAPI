# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:27:07 2016

@author: hujie

Data of games

"""

import urllib
import json
import requests

serviceURL = "http://steamspy.com/api.php?"
url = serviceURL + urllib.urlencode({'request': 'all'})
r = requests.get(url,auth=('account','xxxxxx'))      ## You can register your own API account
# You can use below code to check status
# r.status_code
# r.headers['content-type']
# r.encoding
# r.text
# r.json()

try: js = json.loads(str(r.text).encode('ascii'))
except: js = None


# find None value in json file, convert into string before write them into csv
count = 0
for item in js:
    if js[item]['publisher'] == None:    
        count +=1
        js[item]['publisher'] = 'NA'
    # print js[item]

print "count of None is: ",count

# Output JSON file of data
text_file = open("json_tAPI.txt", "w")
for item in js:  
    if js[item]['publisher']=='Hidden':        
        continue  
    text_file.write(str(js[item]))
    text_file.write("\n\n")

text_file.close()


# write into csv file for further analysis
import csv

with open("SteamSpy_tAPI.csv", 'wb') as wf:
    f = csv.writer(wf)
    f.writerow(["APP_ID", "average_2weeks", "average_forever", "ccu", 
                "developer", "median_2weeks", "median_forever", "name", 
                "owners", "owners_variance","players_2weeks","players_2weeks_variance",
                "players_forever","players_forever_variance","publisher","score_rank"])
    
    for item in js:
        if js[item]['publisher']=='Hidden': 
            continue   
     
        f.writerow([js[item]['appid'], 
                    js[item]['average_2weeks'], 
                    js[item]['average_forever'], 
                    js[item]['ccu'],                            
                    js[item]['developer'].encode('utf-8'),
                    js[item]['median_2weeks'],
                    js[item]['median_forever'],
                    js[item]['name'].encode('utf-8'),
                    js[item]['owners'],
                    js[item]['owners_variance'],
                    js[item]['players_2weeks'],
                    js[item]['players_2weeks_variance'],
                    js[item]['players_forever'],
                    js[item]['players_forever_variance'],
                    js[item]['publisher'].encode('utf-8'),
                    js[item]['score_rank'],
                    ])





