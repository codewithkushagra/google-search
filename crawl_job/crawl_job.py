from urllib.request import urlopen
from bs4 import BeautifulSoup

class CrawlJob:

    def __init__(self, urls):
        self.urls = urls

    def start_crawl_job(self):
        result = []
        for url in self.urls:
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features="html.parser")

            links = [{'link':link.get('href'),'text': link.text} for link in soup.find_all('a')]

            title = soup.find('title').text

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            
            # get text
            text = soup.get_text()

            # append text and url it is fetched from
            result.append({'text': text, 'title': title, 'url': url,'links':links})
        
        return result
