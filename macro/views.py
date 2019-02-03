from django.http import HttpResponse
from django.shortcuts import render
import operator
def macroword(request):
    return render(request,'index.html')


def count(request):
    data = request.GET['fulltext']
    data_list = data.split()
    word_len = len(data_list)
    worddictionary = {}
    for word in data_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1),reverse=True)

    return render(request,'contact.html', {'fulltext':data ,'words_count':word_len,'worddictionary':sorted_list})
def about(request):
    return render(request,'about.html')