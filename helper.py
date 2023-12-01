import numpy as np
import pandas as pd
import requests
import json
import os

clientid=os.getenv('clientid')
clientsecret=os.getenv('clientsecret')
clientkey=os.getenv('clientkey')

def gettoken():
    url = 'https://open.tiktokapis.com/v2/oauth/token/'
    data = {'client_key': clientkey,
           'client_secret': clientsecret,
           'grant_type': 'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, data=data, headers=headers)
    return json.loads(r.text)['access_token']

root = 'https://open.tiktokapis.com/v2/research'
headers = {'Authorization': 'Bearer ' + gettoken(),
          'Content-Type': 'application/json'}
fields = ['id',
         'video_description',
         'create_time', 
         'region_code',
         'share_count',
         'view_count',
         'like_count',
         'comment_count', 
         'music_id',
         'hashtag_names', 
         'username',
         'effect_ids',
         'playlist_id',
         'voice_to_text']
params = {'fields': ','.join(fields)}

def queryvideo(query, start_date, end_date,
               root=root, headers=headers, max_count=100,
               params=params):
    endpoint = '/video/query/'
    data = {'query': json.dumps(json.loads(query)),
            'start_date': start_date,
            'end_date': end_date,
            'max_count': max_count}
    r = requests.post(root+endpoint, headers=headers, params=params, data=data)
    myjson = json.loads(r.text)
    try:
        return (myjson['data']['cursor'],
           myjson['data']['has_more'],
           myjson['data']['search_id'],
           pd.json_normalize(myjson, record_path = ['data', 'videos']))
    except:
        return (r.text, data)
    