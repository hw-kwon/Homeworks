import requests
import webbrowser

search = 'python requests module'
queryString = {'q': search}
searchEngine = 'https://www.google.com/search'
r = requests.get(searchEngine, params = queryString)

print(r.url)
webbrowser.open(r.url)
