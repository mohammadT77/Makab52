# wikipedia_bs.py
import argparse
import logging
import requests

from bs4 import BeautifulSoup

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('query')

    args = parser.parse_args()

    url = f"https://en.wikipedia.org/wiki/{args.query}"
    resp = requests.get(url)
    html_content = resp.text
    file_name = args.query+'.html'
    with open(file_name, 'w') as f:
        f.write(html_content)
        logging.info('File saved at:', file_name)

    bs = BeautifulSoup(html_content, features="lxml")
    ps = bs.find_all('p')
    h1s = bs.find_all('h1')
    h2s = bs.find_all('h2')
    h3s = bs.find_all('h3')
    h4s = bs.find_all('h4')
    h5s = bs.find_all('h5')
    h6s = bs.find_all('h6')

    print(*ps, *h1s, *h2s, *h3s, *h4s, *h5s, *h6s, sep='\n')
