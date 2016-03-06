from bs4 import BeautifulSoup
import requests

start_url = 'http://bj.ganji.com/wu/'
wb_data = requests.get(start_url)
soup = BeautifulSoup(wb_data.text, 'html.parser')
all_links = soup.select('dl.fenlei > dt > a')
links = ['http://bj.ganji.com' + i.get('href') for i in all_links if i.get('href') != '/shoujihaoma/']

def get_item_list(url):
    url_data = requests.get(url)
    url_soup = BeautifulSoup(url_data.text, 'html.parser')
    url_list = url_soup.select('a.ft-tit')
    item_list = [j.get('href') for j in url_list if j.get('href')[7:11] == 'bj.g']
    print(item_list)



get_item_list('http://bj.ganji.com/jiaju/')
