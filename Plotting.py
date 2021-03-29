import matplotlib.pyplot as plt
from collections import Counter
import json
import itertools
import plotly.express as px
f = open('keyword.json','r')
data =json.load(f)
keys = list(data.keys())
data_ = [data[d] for d in (keys) if d.find('content')!=-1]
All_list = (list(itertools.chain.from_iterable(data_)))
Frequency = dict(Counter(All_list))
x = list(Frequency.keys())
y = list(Frequency.values())
print(x,y)
#plt.barh(x,y)
#plt.yticks(rotation=45)
#plt.show()
fig = px.bar( x=y, y=x, orientation='h')
fig.write_image('bar.png',scale=2)
fig.show()
fig = px.pie(values=y, names=x, title='What skills are needed in data science')
fig.write_image('pie.png',scale=2)
fig.show()


