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
        sorted_tuples = sorted(Frequency.items(), key = lambda item:item[1])
        Frequency = {k:v for k, v in sorted_tuples}
        x = list(Frequency.keys())
        y = list(Frequency.values())
        #print(px.colors.cyclical.swatches_cyclical())
        fig_1 = px.bar(x=y, y=x, orientation='h',labels=dict(x="Counts", y="Keywords"),color=y,color_continuous_scale=px.colors.sequential.Emrld)
        fig_1.update_layout(font=dict(family="Times New Roman",
        size=18,
        color="black"))
        #fig_1.update_layout( xaxis={'categoryorder':'category descending'})
        #fig_1.write_image('bar'+file_.split('.')[0]+'.png',scale=2)
        fig_1.show()
        fig_2 = px.pie(values=y, names=x, title='What skills are needed in data science'+'  '+file_.split('.')[0],color_discrete_sequence=px.colors.cyclical.IceFire)
        #fig_2.write_image('pie'+file_.split('.')[0]+'.png',scale=2)
        fig_2.update_layout(font=dict(family="Times New Roman",
        size=18,
        color="black"))
        fig_2.show()

        return([fig_1,fig_2])

if __name__ =='__main__':

    obj = plotter()
    files = glob.glob('*.json')#['keywordJobsCalifornia.json','keywordJobsNew York.json']#glob.glob('*.json')
    for files_ in files:
        list_fig = obj.plot_(files_)
    #print("This is the list",list_fig)


