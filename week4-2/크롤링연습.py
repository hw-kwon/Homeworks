# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.youtube.com/results?search_query='
# qurey = input('찾고싶은 키워드 : ')

# fullurl = url + qurey
# data = requests.get(fullurl).text
# soup = BeautifulSoup(data, 'html.parser')
# youtube_title = soup.find_all(class_='style-scope ytd-video-renderer')
# title_array = []
# for title in youtube_title:
#     title_array.append(title.get('aria-label'))

# print(title_array)

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.melon.com/chart/index.htm')
html = response.content
soup = BeautifulSoup(html, 'html.parser')

list_song = soup.find_all(name='div', attrs={'class': "wrap_song_info"})
list_artists = soup.find_all(name='title', attrs={'class': 'wrap_song_info'})

for index in range(len(list_song)):
    title = list_song[index].find('a').text
    print(index + 1, ':', title)
    if index == 99:
        break


for index in range(len(list_artists)):
    title = list_song[index].find('span').text
    print(index + 1, ':', title)
    if index == 99:
        break
