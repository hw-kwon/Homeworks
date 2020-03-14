import requests
import webbrowser

google_map_url: 'https://maps.googleapis.com/maps/api/geocode/json'
params: {'address': 'seoul', 'key': ''}

req = requests.get(google_map_url, params=params)
print(req.url)

res = req.json()['results']
location = res[0]['geometry']['location']
print(location['lat'], location['lng'])
