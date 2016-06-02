# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:27:07 2016

@author: hujie
"""

import urllib
import json
import requests

serviceURL = "http://steamspy.com/api.php?"
    
url = serviceURL + urllib.urlencode({'request': 'top100in2weeks'})

r = requests.get(url,auth=('oefox000000','Yangjq@2008'))

r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()

# below part is crawling program not suitable for API
# print 'Retrieving', url
# uh = urllib.urlopen(url)
# data = uh.read()
# print 'Retrieved', len(data), 'characters'

try: js = json.loads(str(r.text))
except: js = None

for item in js:
    print js[item]['appid']
# List all content I get from SteamSpy
for item in js:
    print 'APP ID:   ', js[item]['appid']
    print 'Name:     '  , js[item]['name']
    print 'Developer:', js[item]['developer']
    print 'Rank:     ', js[item]['score_rank']
    print 'Owners:   ', js[item]['owners']
    print 'Player4ever: ', js[item]['players_forever']
    print 'Player2weeks: ', js[item]['players_2weeks']
    print 'Avg.PlayTime in 2 weeks: ', js[item]['average_2weeks']
    print 'Median.TotalPlayTime: ', js[item]['median_forever']
    print 'YesterdayCCU: ',js[item]['ccu']
    
    
# write into csv file for further analysis
import csv

with open("SteamSpy.csv", 'wb') as wf:
    f = csv.writer(wf)
    f.writerow(["APP_ID", "Name", "Publisher", "Developer", "Rank", "Owners", "TotalPlayer", "TotalPlayersOf2weeks", "AvgPlayTimeIn2weeks", "Median.TotalPlayTime","YesterdayCCU"])
    for item in js:
        if js[item]['publisher']=='Hidden': 
            continue   
        
        f.writerow([js[item]['appid'], 
                    js[item]['name'].encode('utf-8'), 
                    js[item]['publisher'].encode('utf-8'), 
                    js[item]['developer'].encode('utf-8'),
                    js[item]['score_rank'],
                    js[item]['owners'],
                    js[item]['players_forever'],
                    js[item]['players_2weeks'],
                    js[item]['average_2weeks'],
                    js[item]['median_forever'],
                    js[item]['ccu']])


# Output JSON file of data
text_file = open("json.txt", "w")
for item in js:  
    if js[item]['publisher']=='Hidden':        
        continue  
    text_file.write(str(js[item]))
    text_file.write("\n\n")

text_file.close()


