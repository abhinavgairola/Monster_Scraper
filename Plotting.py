import matplotlib.pyplot as plt
from collections import Counter
import json
import itertools
import plotly.express as px
import glob

class plotter:

    def plot_(self, file_):
        f = open(file_,'r')
        data =json.load(f)
        keys = list(data.keys())
        data_ = [data[d] for d in (keys) if d.find('content')!=-1]
        All_list = (list(itertools.chain.from_iterable(data_)))
        Frequency = dict(Counter(All_list))
        x = list(Frequency.keys())
        y = list(Frequency.values())
        fig_1 = px.bar( x=y, y=x, orientation='h')
        fig_1.update_layout( xaxis={'categoryorder':'category descending'})
        fig_1.write_image('bar'+file_.split('.')[0]+'.png',scale=2)
        fig_1
        fig_2 = px.pie(values=y, names=x, title='What skills are needed in data science'+'  '+file_.split('.')[0])
        fig_2.write_image('pie'+file_.split('.')[0]+'.png',scale=2)
        fig_2.show()

        return([fig_1,fig_2])

if __name__ =='__main__':

    obj = plotter()
    files = glob.glob('*.json')#['keywordJobsCalifornia.json','keywordJobsNew York.json']#glob.glob('*.json')
    for files_ in files:
        list_fig = obj.plot_(files_)
    #print("This is the list",list_fig)


