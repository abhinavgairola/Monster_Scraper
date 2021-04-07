import pandas as pd 
import csv
import requests
import json
import os
from bs4 import BeautifulSoup
import re
import glob

class linkParsing:

    def __init__(self):
        return None
    
    def folders(self):
        list_ = [name for name in os.listdir() if os.path.isdir(name) ]
        print("This is the list_",list_)
        list_.remove('.ipynb_checkpoints')
        #print("This is the list",list_)
        return list_

    def link_picker(self, csvfile):

        f = open(csvfile,'r')
        filecontent = csv.reader(f)
        headers = next(filecontent)

        matches = ['python','pandas','matplotlib','plotly','matlab','jupyter','aws','sql','spark','pyspark','quantitative','engineering','scikit-learn','numpy','associate']

        pattern = re.compile('|'.join(matches))
        #pattern = re.compile(r'(fedramp|nist|aws|cissp|security clearance)')
        print("This is the pattern", pattern)
        
        corpus = {}
        links = {}
        for idx,line in enumerate(filecontent):
            print('='*100)
            print("Looking for keywords in link number {}".format(idx))
            print('='*100)
            content = []
            urllink = requests.get(line[1])
            soup = BeautifulSoup(urllink.content, 'html.parser')
            text_list =(soup.text.lower())

            temp = (re.findall(pattern,text_list))
            if len(temp)/len(matches)>=0.2:
                unique_list = []
                for t in temp:
                    if t not in unique_list:
                        unique_list.append(t)
                corpus[str(idx)+' '+'content'] = unique_list
                print(unique_list)
                links[str(idx)+' '+'link'] = line[1]
            
        return (corpus,links)


if __name__ == '__main__':
    obj = linkParsing()
    folders = obj.folders()
    for fol in folders:
        file_list = glob.glob(fol+'/'+'*.csv')
        print("This is the file_list",file_list)
        for file_ in file_list:
            file__  = file_.split('/')[1]
            print("This is the next",file__)
            data,data_2 = obj.link_picker(file_)
            f = open(fol+'/'+'keyword'+file__.split('.')[0]+'.json','w')
            data.update(data_2)
            print(data)
            json.dump(data,f)
