# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:31:36 2021

@author: info
"""

#I HAVE CREATED THIS FILE -RAJAT GARG
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # params={'name':'rajat','place':'INDIA'}
    return render(request,'index.html')
    #return HttpResponse('''<h1>HOMEPAGE</h1><a href ="https://www.linkedin.com/mynetwork/"> MYProfile linkedin</a>''')

def about(request):
    return HttpResponse('''<h1>RAJAT GARG</h1><a href="https://www.youtube.com/results?search_query=Rajat+garg+a+simple+magic+trick">Django with Rajat</a>''')
def also(request):
    file=open("1.txt")
    return HttpResponse(file.read())
def noise(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/"> GOTO HOMEPAGE</a>''')
def analyze(request):
    #GETTING THE TEXT
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    #analyzed=djtext
    if removepunc=="on":
         punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
         analyzed=""
         for char in djtext:
            if char not in punctuations:
               analyzed=analyzed+char
         params={'purpose':'Rmoved punctuations', 'analyzed_text':analyzed}
         #ANALYSING THE TEXT
         return render(request,'analyze.html',params)
         #return HttpResponse("remove punc")
    else:
        return HttpResponse("ERROR")