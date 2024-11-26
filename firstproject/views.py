from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'homepage.html')
def analyze(request):
    djtext=request.POST.get('text','defaultvalue')
    fullcaps=request.POST.get('uppercase','off')
    removepunc=request.POST.get('removepunc', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    space_remover=request.POST.get('space_remover','off')
    analyzed_text=djtext
    newtext = ''
    if removepunc == 'on':
        a='''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyzed_text=''
        b=''
        for k in djtext:
            if k in a:
                continue
            else:
                analyzed_text=analyzed_text+k
        param= {'purpose':'removed punctuations','analyzed_text':analyzed_text}
    if space_remover=='on':
        b=''
        for k in analyzed_text:
            if k==' ':
                continue
            else:
                b=b+k
        analyzed_text=b
        param= {'purpose':'removed space','analyzed_text':analyzed_text}                    
    if fullcaps == 'on':
        analyzed_text=analyzed_text.upper()
        param= {'purpose':'changed to uppercase','analyzed_text':analyzed_text}
    if newlineremover=='on':
        for k in analyzed_text:
            if k=="\n" or k=="\r":
                continue
            else:
                newtext=newtext+k 
        analyzed_text=newtext
        param= {'purpose':'removed new lines','analyzed_text':analyzed_text}        
    return render(request,'analyze.html',param)     
def aboutus(request):
    return render(request,'aboutus.html')
