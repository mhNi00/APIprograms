import requests
import json
import re
url = 'https://www.virustotal.com/vtapi/v2/file/report'
key = input("Insert the hash of the file you want to check, and i'll give you info on how many different vendors it was detected as harmful!")
params = {'apikey': '', 'resource': key}
sum_of_detects = 0
response = requests.get(url, params)
lib_of_vendors = ['Bkav','Elastic','MicroWorld-eScan','CMC','CAT-QuickHeal','Qihoo-360','ALYac','Cylance','Zillya','AegisLab','Sangfor','CrowdStrike','Alibaba','K7GW','K7AntiVirus','Baidu','Cyren','Symantec','ESET-NOD32','APEX','Avast','ClamAV','Kaspersky','BitDefender','NANO-Antivirus','ViRobot','Tencent','Ad-Aware','TACHYON','Emsisoft','Comodo','F-Secure','DrWeb','VIPRE','TrendMicro','FireEye','Sophos','SentinelOne','GData','Jiangmin','Webroot','Avira','Kingsoft','Gridinsoft','Arcabit','SUPERAntiSpyware','ZoneAlarm','Microsoft','Cynet','AhnLab-V3','Acronis','McAfee','MAX','VBA32','Malwarebytes','Panda','Zoner','TrendMicro-HouseCall','Rising','Yandex','Ikarus','eGambit','Fortinet','BitDefenderTheta','AVG','Cybereason','Paloalto','MaxSecure']
for i in range(len(lib_of_vendors)):
    try:
        if response.json()['scans'][lib_of_vendors[i]]['detected'] == True:
            sum_of_detects += 1
    except:
        KeyError
if sum_of_detects > 0:
    print("This file has been marked as malware by",sum_of_detects,"vendors! I wouldn't trust this file...")
else:
    print("File seems to be safe :)")
