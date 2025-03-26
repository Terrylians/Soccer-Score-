import numpy as np 
import pandas as pd 
import requests
from bs4 import BeautifulSoup
import json



import matplotlib.pyplot as plt

url = 'https://understat.com/match/27233'

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
scripts = soup.find_all('script')

strings = scripts[1].string

ind_start = strings.index("('")+2
ind_end = strings.index("')")
json_data = strings[ind_start:ind_end]
json_data = json_data.encode('utf8').decode('unicode_escape')
data=json.loads(json_data)

player = []
shotType = []
x = []
y = []
xG = []
playerAssisted = []
result = []
team = []
data_away = data['a']
data_home = data['h']

for index in range(len(data_home)):
    for key in data_home[index]:
        if key == 'player':
            player.append(data_home[index][key])
        if key == 'shotType':
            shotType.append(data_home[index][key])
        if key == 'player_assisted':
            playerAssisted.append(data_home[index][key])
        if key == 'X':
            x.append(data_home[index][key])
        if key == 'Y':
            y.append(data_home[index][key])
        if key == 'h_team':
            team.append(data_home[index][key])
        if key == 'xG':
            xG.append(data_home[index][key])
        if key == 'result':
            result.append(data_home[index][key])

for index in range(len(data_away)):
    for key in data_away[index]:
        if key == 'player':
            player.append(data_home[index][key])
        if key == 'shotType':
            shotType.append(data_home[index][key])
        if key == 'player_assisted':
            playerAssisted.append(data_home[index][key])
        if key == 'X':
            x.append(data_away[index][key])
        if key == 'Y':
            y.append(data_away[index][key])
        if key == 'a_team':
            team.append(data_away[index][key])
        if key == 'xG':
            xG.append(data_away[index][key])
        if key == 'result':
            result.append(data_away[index][key])

df = pd.DataFrame({'player':player,'shotType':shotType,'playerAssisted':playerAssisted,'x':x,'y':y,'xG':xG,'result':result,'team':team})
print(df.head(5))

df['player'].value_counts()
df['shotType'].value_counts()
df['playerAssisted'].value_counts()
df['result'].value_counts()
df['team'].value_counts()


import seaborn as sns
sns.set_style('whitegrid')
plt.figure(figsize=(12,6))
plt.scatter(df['x'],df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Shot chart')
plt.gca().invert_yaxis()


plt.show()