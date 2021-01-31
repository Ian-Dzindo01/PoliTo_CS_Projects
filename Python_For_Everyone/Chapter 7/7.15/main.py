from bs4 import BeautifulSoup
import requests
import re

href_urls = []
# href_urls1 = []

response = requests.get("http://lite.cnn.com/en", verify=False)
soup = BeautifulSoup(response.content)
for link in soup.findAll('a'):
    href_urls.append((link.get('href')))

print(href_urls)


# The problem with going through all the links supplied on the website is that many of them lead back to the same source that we are reading from.
# Also there will be problems with the http:// prefix, which is absent in most of these links. Simply appending it at the beginning does not fix the problem.


# for url in href_urls:
#     response = requests.get('https://'+url, verify=False)
#     soup = BeautifulSoup(response.content, "html.parser")

#     for link in soup.findAll('a'):
#         href_urls1.append((link.get('href')))
