
import requests
from bs4 import BeautifulSoup
urlst = 'https://quotes.toscrape.com/'
autor_dict = {}
responsest = requests.get(urlst)

if responsest.ok:
    url = 'https://quotes.toscrape.com/page/1/'
    x = 1
    while x == 1:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.select('div[class="quote"]')
        if 'Next' in soup.ul.text:
            x = 1
            next = soup.select('li[class="next"]')
            for na in next:
                href2 = na.select_one('a').get('href', '')
                url = 'https://quotes.toscrape.com' + href2
                for quote in quotes:
                    text = quote.select_one('span[class="text"]').text.strip().replace('“', '').replace('”', '')
                    author = quote.select_one('small[class="author"]').text
                    href = quote.select_one('a').get('href', '')
                    if href:
                        href = urlst + href[1:]
                    author_response = requests.get(href)
                    author_soup = BeautifulSoup(author_response.text, 'lxml')
                    b_day = author_soup.select_one('span[class="author-born-date"]').text
                    location = author_soup.select_one('span[class="author-born-location"]').text
                    if author not in autor_dict:
                        autor_dict[author] = {'b_day: ': None, 'Location: ': None, 'Things: ': []}
                        if autor_dict[author]['b_day: '] == None:
                            autor_dict[author]['b_day: '] = b_day
                        if autor_dict[author]['Location: '] == None:
                            autor_dict[author]['Location: '] = location
                    if author in autor_dict:
                        autor_dict[author]['Things: '].append(text)
        else:
            x = 0
            for quote in quotes:
                text = quote.select_one('span[class="text"]').text.strip().replace('“', '').replace('”', '')
                author = quote.select_one('small[class="author"]').text
                href = quote.select_one('a').get('href', '')
                if href:
                    href = urlst + href[1:]
                author_response = requests.get(href)
                author_soup = BeautifulSoup(author_response.text, 'lxml')
                b_day = author_soup.select_one('span[class="author-born-date"]').text
                location = author_soup.select_one('span[class="author-born-location"]').text
                if author not in autor_dict:
                    autor_dict[author] = {'b_day: ': None, 'Location: ': None, 'Things: ': []}
                    if autor_dict[author]['b_day: '] == None:
                        autor_dict[author]['b_day: '] = b_day
                    if autor_dict[author]['Location: '] == None:
                        autor_dict[author]['Location: '] = location
                if author in autor_dict:
                    autor_dict[author]['Things: '].append(text)
    print(autor_dict)
if __name__ == '__main__':
    pass
