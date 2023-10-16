# First we import the required libraries:

import requests
from bs4 import BeautifulSoup

# Secondly, we  use the "requests" library to send a "get" request and store the response in a variable "r".

url = "https://www.python.org/"
r = requests.get(url)

# Create a BeautifulSoup object from the response and parse it.
soup = BeautifulSoup(r.content, 'html.parser')

# Using the "find" and "findall" functions to separate <div> tags with a class of "shrubbery" as they contain the "latest news articles"
news_list = soup.find("div", class_="shrubbery").find_all("li")

# Use "for" loop to iterate through the articles and scrape the title and summary.
# We use the ".text" attribute.

for news in news_list:
    scraped_data = (f"- {news.text.strip()}")
    data = open('D:\\DigiCrome\\scraped_data.txt','a',encoding="utf-8")
    data.write(scraped_data)
    data.close()


# For word frequency:

# Open the file in read mode
wf = open('D:\\DigiCrome\\scraped_data.txt','r')

# Create an empty dictionary
dic = dict()

# Loop through each line of the file 

for line in wf:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    # Iterate over each word in line 
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1

for key in list(dic.keys()):
    print(key, ":", dic[key])
    