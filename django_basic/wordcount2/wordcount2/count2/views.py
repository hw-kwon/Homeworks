from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):
    text = request.GET['fulltext']
    textcount = len(text)
    divide = text.split()
    dic = {}
    for i in divide:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return render(request, 'result.html', {'text': text, 'textcount': textcount, 'divide': divide, 'i': i, 'dic': dic})
