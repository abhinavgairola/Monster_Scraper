import matplotlib.pyplot as plt
from collections import Counter
import json
import itertools
import plotly.express as px

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
        fig_1.write_image('bar.png',scale=2)
        fig_1
        fig_2 = px.pie(values=y, names=x, title='What skills are needed in data science')
        fig_2.write_image('pie.png',scale=2)
        fig_2.show()

        return([fig_1,fig_2])

if __name__ =='__main__':

    obj = plotter()
    list_fig = obj.plot_('keyword.json')
    #print("This is the list",list_fig)


