import bs4 as bs
from urllib.request import Request,urlopen
import csv
def insert_method(url):
    sauce=Request(str(url),None,{'User-Agent':'Mozilla/5.0'})
    webpage=urlopen(sauce).read()
    soup=bs.BeautifulSoup(webpage,'lxml')
    #ds=bs.BeautifulSoup(soup.findAll("dd",{"class":"episodes"}))
    i=0
    with open('file.csv','a') as csvfile:
        fieldnames=['id','title','link']
        writer=csv.DictWriter(csvfile,fieldnames)
        writer.writeheader()
        for link in soup.findAll('li',{'class':'link'}):
            i=i+1
            #print(link.find('a')['title'])
            writer.writerow({'id':i,'title':link.find('a')['title'],'link':link.find('a')['href']})
        print("writing complete")
#db.season_entry(i,link.find('a')['title'],link.find('a')['href'],"Episodes")
#db.close_conn()

    
