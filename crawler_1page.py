import requests
from bs4 import BeautifulSoup

# From URL of one particular website, get its content
url = "https://www.indeed.com/cmp/Om-Computers/jobs/Data-Scientist-41e194d945c32e50?q=data+scientist&vjs=3"
# this website may expire. 
response = requests.get(url)
html = response.content

# grub the main body of website
soup = BeautifulSoup(html,features="html5lib")
body = soup.find(name = "body")

# grub the job description information
text = body.find("div", attrs = {'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'})

# record company's name
company = body.find("div", attrs = {'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'})
company_name = company.text

# record job title
title = body.find("h3", attrs = {'class':'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'})
title_name = title.text

# write the job description into a .txt file named by the company's name
with open(company_name+'.txt','xt') as content:
    content.write(title_name)
    content.write('\n')
    content.write(company_name)
    content.write('\n')
    for row in body.find("div", attrs = {'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'}):
        content.write(row.text)
        content.write('\n')
