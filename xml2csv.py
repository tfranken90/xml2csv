import xml.etree.ElementTree as ET
import datetime
import time 
import pandas as pd

root = ET.parse('sample.xml').getroot()

output = pd.DataFrame()

for child in root.findall('channel/item'):
    episode = {}

    for tag in child.findall('{http://www.itunes.com/dtds/podcast-1.0.dtd}episode'):
        episode.update({"rel0_attr0_text": tag.text})
    
    for tag in child.findall('{http://www.itunes.com/dtds/podcast-1.0.dtd}title'):
        episode.update({"name": tag.text})
    
    for tag in child.findall('{http://www.itunes.com/dtds/podcast-1.0.dtd}duration'):
        episode.update({"length": tag.text})
    
#    for tag in child.findall('pubDate'):
#        date = datetime.datetime.strptime(tag.text, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d')
#        episode.update({"date": date})
    
    for tag in child.findall('enclosure'):
        episode.update({"url0_url": tag.get('url')})

    output = output._append(episode, ignore_index=True)

output.iloc[::-1].to_csv('out.csv',index=False,header=True)

