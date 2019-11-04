# WebCrawler_DSJob
A web crawler for grabbing Data Scientist  job description/requirement in **Indeed**.  

(Since it needs specific name attributes, this web crawler only can use in Indeed websites.)

When I do job searching for data scientist in Indeed, there exist plenty of companies and each of them has its unique job description and requirement. It 's a waste of time to click every website. It's not hard to find that all the job websites have the same structure in Indeed. 

So I ask what a **data scientist** will do in this situation? 

***Write a web crawler!***

First, I need a function to grab information from one specific website and write it into a new .txt file with the name of the company.

Then, I need to scrape the company list in the search website in Indeed, with setting the job "Data Scientist" and the area "New York". Find the URL for each job, apply the formal function to each.

And Voila!



![demo_list](https://github.com/Jiashuo-Sun/WebCrawler_DSJob/blob/master/demo_picture/demo_list.png)

![demo_concept](https://github.com/Jiashuo-Sun/WebCrawler_DSJob/blob/master/demo_picture/demo_concept.png)