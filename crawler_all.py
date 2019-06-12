import requests
from bs4 import BeautifulSoup

# grab description in each specific website
def get_describe(urlname):
    try:
        url = urlname
        response = requests.get(url)
        html = response.content
    
        soup = BeautifulSoup(html,features="html5lib")
        body = soup.find(name = "body")
    
        company = body.find("div", attrs = {'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'})
        company_name = company.text

        title = body.find("h3", attrs = {'class':'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'})
        title_name = title.text
    
        with open(company_name+'.txt','xt') as content:
            content.write(title_name)
            content.write('\n')
            content.write(company_name)
            content.write('\n')
            for row in body.find("div", attrs = {'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'}):
                content.write(row.text)
                content.write('\n')
    except:
        print(working)
        

url = "https://www.indeed.com/jobs?q=data+scientist&l=New+York%2C+NY"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,features="html5lib")
body = soup.find(name = "td", attrs = {'id':'resultsCol'})

test = body.find_all("a")
for names in test:
    urlname = names.get('href')
    try:
        if ((urlname != None) & (len(urlname) >= 3)):
            urlname = 'https://www.indeed.com' + urlname
            get_describe(urlname)
    except:
        continue