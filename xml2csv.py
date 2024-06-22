import xml.etree.ElementTree as ET
import datetime
import time 
import pandas as pd

root = ET.parse('sample.xml').getroot()


#dict = {'number': 0, 'title': 'titles', 'url': 'urls', 'date': 'dates', 'length': 'lengths', 'description': 'desc'}

#episodes = pd.DataFrame(dict)

output = pd.DataFrame()

for child in root.findall('channel/item'):
    episode = {}

    for tag in child.findall('{http://www.itunes.com/dtds/podcast-1.0.dtd}episode'):
        episode.update({"number": tag.text})
    
    for tag in child.findall('{http://www.itunes.com/dtds/podcast-1.0.dtd}title'):
        episode.update({"title": tag.text})
    
    for tag in child.findall('{http://www.itunes.com/dtds/podcast-1.0.dtd}duration'):
        #x = time.strptime(tag.text,'%H:%M:%S')
        #seconds = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        episode.update({"duration": tag.text})

#        seconds = int(tag.text)
#        time = str(datetime.timedelta(seconds=seconds))
#        lengths.append(time)
    
    for tag in child.findall('pubDate'):
        date = datetime.datetime.strptime(tag.text, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d')
        episode.update({"date": date})
    
    for tag in child.findall('enclosure'):
        episode.update({"url": tag.get('url')})

    output = output._append(episode, ignore_index=True)

output.iloc[::-1].to_csv('out.csv',index=False,header=False)


#df = pd.DataFrame(dict)

#    print(i.get(title.text))
#    for title in i.get('title'):
#        print(title.text)


#episode = []
#name = []
#urls = []
#length = []
#dates = []
#desc = []

#for tag in root.findall('channel/item/{http://www.itunes.com/dtds/podcast-1.0.dtd}episode'):
#    episode.append(tag.text)
#
##for tag in root.findall('channel/item/title'):
#for tag in root.findall('channel/item/{http://www.itunes.com/dtds/podcast-1.0.dtd}title'):
#    name.append(tag.text)
#
#for tag in root.findall('channel/item/description'):
#    desc.append(tag.text)
#
#for tag in root.findall('channel/item/{http://www.itunes.com/dtds/podcast-1.0.dtd}duration'):
#    #seconds = int(tag.text)
#    #time = str(datetime.timedelta(seconds=seconds))
#    #lengths.append(time)
#    length.append(tag.text)
#
#for tag in root.findall('channel/item/pubDate'):
#    date = datetime.datetime.strptime(tag.text, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d')
#    dates.append(date)
#
#for tag in root.findall('channel/item/enclosure'):
#    urls.append(tag.get('url'))
#
#dict = {'title': titles, 'url': urls, 'date': dates, 'length': lengths, 'description': desc}
#dict = {'date': dates, 'title': titles, 'url': urls}
#dict = {'episode': episode, 'name': name, 'length': length, 'date': dates, 'url': urls} 

