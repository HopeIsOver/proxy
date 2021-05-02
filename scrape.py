import re,requests, sys
from bs4 import BeautifulSoup
def Scrape(u):
    try:
        t = "\n"
        d = requests.get(u).text
        soup = BeautifulSoup(d, features="html.parser")
        for script in soup(["script","style","td","abbr"]):
            script.extract()
        text = soup.get_text()
        for ligne in text.split("\n"):
            if(re.match("((?:1?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(?:1?\d{1,2}|2[0-4]\d|25[0-5]):\d{2,5}",ligne)):
                t += ligne + "\n"
        return t
    except:
        pass
with open("links","r") as f:
    data = f.read().split("\n")
    f.close()

total = ""
for url in data:
    try:
        total += Scrape(url)
    except:
        pass

with open("proxies","w+") as f:
    f.write(total)
    f.close()
