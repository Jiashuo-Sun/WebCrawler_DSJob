import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/cmp/Om-Computers/jobs/Data-Scientist-41e194d945c32e50?q=data+scientist&vjs=3"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,features="html5lib")
body = soup.find(name = "body")

text = body.find("div", attrs = {'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'})

#print(text)
#print(text.prettify())
#for row in body.find("div", attrs = {'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'}):
    #print(row.prettify())
    #print(row.text)

company = body.find("div", attrs = {'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'})
company_name = company.text

title = body.find("h3", attrs = {'class':'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'})
title_name = title.text

#print(company_name)
with open(company_name+'.txt','xt') as content:
    content.write(title_name)
    content.write('\n')
    content.write(company_name)
    content.write('\n')
    for row in body.find("div", attrs = {'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'}):
        content.write(row.text)
        content.write('\n')