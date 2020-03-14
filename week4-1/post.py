import requests, json

github_url = 'https://api.github.com/user/repos'

data = json.dumps({'name':'test', 'description':'some test repo'})
r = requests.post(github_url,data = data, auth = ('hw-kwon','hyeonda94!'))
print(r.json)