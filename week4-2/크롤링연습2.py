import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/results?search_query='
query = input('유튜브 검색 : ')
fullurl = url + query
res = requests.get(fullurl).text
soup = BeautifulSoup(res, 'html.parser')
youtube_title = soup.find_all(
    class_='yt-simple-endpoint style-scope ytd-video-renderer')
title_array = []

for title in youtube_title:
    title_array.append(title.get('title'))

print(title_array)
