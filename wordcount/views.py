import operator

from django.http import  HttpResponse
from django.shortcuts import  render

def homepage(request):
    return render(request,'home.html')


def count(request):
    key=request.GET['fulltext']
    wordcount = key.split()
    worddictionary = {}
    for word in wordcount:
        if word in worddictionary:
        #increment it
            worddictionary[word]+=1
        else:
        #keep it as 1
            worddictionary[word]=1
    SortedWords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=False)

    # return render(request,'count.html',{'key':key,'wordcounts':len(wordcount),'worddictionary':worddictionary}) # Approach1
    return render(request,'count.html',{'key':key,'wordcounts':len(wordcount),'worddictionary':worddictionary.items(),'SortedWords':SortedWords}) # Approach2

def about(request):
    return render(request,'about.html')