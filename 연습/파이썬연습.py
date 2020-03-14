'''
def functionEX(params1, params2):
    params1 = params1 + '_VN'
    return (params1, params2)


output = functionEX('LikeLion', 1)
print(output)
'''


'''
class classname:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result = self.result + num
        return self.result


cal1 = classname()
cal2 = classname()

print(cal1.adder(5) + cal2.adder(12))
'''

'''
class practice:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def subtract(self):
        result = self.first - self.second
        return result

    def adder(self):
        result = self.first + self.second
        return result


output = practice(5, 9)

print(output.subtract())
print(output.adder())
'''

'''
import requests
import webbrowser
search = '코로나'
queryString = {'q': search}
searchEngin = 'https://www.google.com/search'
r = requests.get(searchEngin, params=queryString)

print(r.url)
webbrowser.open(r.url)
'''
