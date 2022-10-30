# Implementation of web scrapping lies here, using libraries of beautiful soup and requests to gain data
# NOTE: please install requests and beautiful soup locally
# requests --> gives us the URL's directly to work with for beautiful soup web scrapping
# Beautiful Soup --> manually scrapes the information through the requests objects created

import requests

r = requests.get('https://www.gardenia.net/plants/plant-types')
