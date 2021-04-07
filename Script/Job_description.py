import pandas as pd 
import csv
import requests
import json
from bs4 import BeautifulSoup
import re
import glob

class linkParsing:

    def __init__(self):
        return None

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
            if len(temp)/len(matches)>=0.5:
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
    file_list = glob.glob('*.csv')
    for file_ in file_list:
        print(file_)
        data,data_2 = obj.link_picker(file_)
        f = open('keyword'+file_.split('.')[0]+'.json','w')
        data.update(data_2)
        print(data)
        json.dump(data,f)
