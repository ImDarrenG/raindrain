import requests as http
import urllib
import shutil
import os.path
from datetime import datetime

api_key = 'xxxxxxxxxxx'
api_url = 'http://datapoint.metoffice.gov.uk/public/data/layer/wxobs/all/json/capabilities?key='
rainfall_displayname = 'Rainfall'

json = http.get(api_url + api_key).json()

base_url = json['Layers']['BaseUrl']['$']
data_path = '/home/pi/weather/data'
path_fmt = '{0}/{1}.png'

rainfall_spec = [x for x in json['Layers']['Layer'] if x['@displayName'] == rainfall_displayname][0]['Service']
img_format = rainfall_spec['ImageFormat']
layer_name = rainfall_spec['LayerName']

for t in rainfall_spec['Times']['Time']:
    time = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S')
    img_path = path_fmt.format(data_path, time.strftime('%Y-%m-%d-%H-%M-%S'))
    
    if not os.path.isfile(img_path):
        img_url = base_url.format(LayerName=layer_name, ImageFormat=img_format, Time=t, key=api_key)
        
        img_r = http.get(img_url, stream=True)
        if img_r.status_code == 200:
            with open(img_path, 'wb') as f:
                img_r.raw.decode_content = True
                shutil.copyfileobj(img_r.raw, f) 
