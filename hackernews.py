import requests
import sys
import json
import validators
from bs4 import BeautifulSoup

def hackernews(posts):

    #Instantiating variables

    #Holds the address for the website to be scraped
    response = requests.get('https://news.ycombinator.com/')

    #Uses the BeautifulSoup library to extract the html from the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    #Creates a list to store the information for each article from the html
    articles = soup.find_all(class_='athing')

    pageIndex = 1

    #This loop ensures we have scraped enough pages of the website 
    #to print the required number of articles
    while len(articles) <= posts:
        pageIndex += 1
        newSoup = BeautifulSoup(requests.get('https://news.ycombinator.com/news?p=' + str(pageIndex)).text,'html.parser')
        articles.extend(newSoup.find_all(class_='athing'))

    article_num = 1

    #Iterates over the articles to extract the relevant pieces of information 
    #for each article from the html; in each instance we also check to ensure
    #that the data that will be printed is of the required type and format
    for article in articles:

        title = article.find(class_='storylink').get_text()
        if not title or not isinstance(title, str) or len(title) > 256:
            title = "Unknown"

        uri = article.find_all('td')[-1].a.get('href')
        if not validators.url(uri):
            uri = "URI was invalid"

        author = article.findNext('tr').find_all('td')[1].find_all('a')[0].get('href').split('user?id=')[1]
        if not author or not isinstance(author, str) or len(author) > 256:
            author = "Unknown"

        points = int(article.findNext('tr').find_all('td')[1].find_all('span')[0].get_text().split(' points')[0])
        if not isinstance(points, int) or points < 0:
            points = 0

        comments = article.findNext('tr').find_all('td')[1].find_all('a')[3].get_text().split('\xa0comment')[0].split('discuss')[0]
        if not comments:
            comments = 0
        comments = int(comments)
        if not isinstance(comments, int) or comments < 0:
            comments = 0

        rank = int(article.find_all('span')[0].get_text().split('.')[0])
        if not isinstance(rank, int) or rank < 0:
            rank = 0

        #Constructs an object containing the extracted pieces of data
        obj = {
            "title": title,
            "uri": uri,
            "author": author,
            "points": points,
            "comments": comments,
            "rank": rank
        }

        #Prints the above object in the JSON format
        print(json.dumps(obj, indent=4))

        article_num += 1

        #Terminates the loop when the required number of articles has been printed
        if article_num > posts:
            break

#Allows the method to be run from the command line with the command:
#python3 hackernews.py 'posts'; where 'posts' is the number of articles
#you would like the method to print to the screen
posts = int(sys.argv[1])
hackernews(posts)
