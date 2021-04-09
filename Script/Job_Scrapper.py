import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pandas as pd

Options = Options()
Options.headless = True

class googlesearch:
    def __init__(self):
        self.driver = webdriver.Firefox(options=Options)
        self.driver.implicitly_wait(20)
        return None 

    def create_folder(self,title):
        folder_name = '_'.join(title.split(' '))
        if os.path.exists(folder_name)==False:
            os.mkdir(folder_name)
        return folder_name


    def Monster(self, jobtitle,location, start, end):
        """
        Extract the jobs and the titles of the jobs from Monster 
        """
        url = 'https://www.monster.com/jobs/search?'
        print(url+'q='+jobtitle+'&where='+location+'&stpage='+start+'&page='+end)
        self.driver.get(url+'q='+jobtitle+'&where='+location+'&stpage='+start+'&page='+end)

        Companies = (self.driver.find_elements_by_css_selector("[name*='card_companyname']"))
        Link = (self.driver.find_elements_by_css_selector("[class*='view-details-link']"))
        
        titles = [x.text for x in Companies]
        links = [x.get_attribute('href') for x in Link]
        return(titles, links)



if __name__ =='__main__':
    obj = googlesearch()
    
    Companies = {}
    Links = {}
    ## Supply the number of pages to be scraped ##TODO can be improved later on
    strt = 1
    end = 50
    Jobtitle = 'Data Science'
    foldername = obj.create_folder(Jobtitle)
    Location = 'California'
    Location_Lists = ['North Carolina']#['New York','Washington DC','California','Texas','Kansas','Illinois']
    for lok in Location_Lists:
        for i in range(strt,end,11):
            titles, links = obj.Monster(Jobtitle,lok,str(i),str(i+10))

            Companies[i] = titles
            Links[i] = links
        df=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in Companies.items() ]))
        df_2=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in Links.items() ]))
        df =pd.concat([df.stack(),df_2.stack()],axis=1,ignore_index=True)
        df.dropna().rename(columns={0:'Companies',1:'Links'}).to_csv(foldername+'/'+'Jobs'+lok+'.csv',index=False)
        #print("This is data",df)

