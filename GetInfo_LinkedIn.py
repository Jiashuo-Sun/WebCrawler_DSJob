import requests
from bs4 import BeautifulSoup
from datetime import datetime

while True:	
	url = input(str("Input the URL:\n"))
	url = url.split('?')[0]
	
	if url == 'quit' or url == 'exit':
		break

	html = requests.get(url).content
	soup = BeautifulSoup(html,features="html5lib")
	body = soup.find(name = "body")

	job_title = body.find("h1", attrs = {"class":"topcard__title"}).text

	company = body.find('span', attrs = {'class':'topcard__flavor'}).text

	location = body.find('span', attrs = {'class':'topcard__flavor topcard__flavor--bullet'}).text

	with open('ApplyResult.txt', mode = 'a') as f:
		f.write(str(datetime.date(datetime.today()))+'\t')		
		f.write(job_title+'\t')
		f.write(company+'\t\t')
		f.write(location+'\t')
		f.write(url+'\n')
	
	print('Information is recorded! \n')



