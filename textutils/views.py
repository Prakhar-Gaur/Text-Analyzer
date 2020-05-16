
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello World")

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    stob = request.POST.get('stob', 'off')
    btos = request.POST.get('btos', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps== "on":
        analyzed = ""
        for char in djtext:

            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":

                analyzed = analyzed + char

        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate (djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    if stob=="on":
        res = ''.join(format(ord(i), 'b') for i in djtext)
        analyzed = str(res)
        params = {'purpose': 'String To Binary', 'analyzed_text': analyzed}
        djtext = analyzed



    if removepunc=="on" or fullcaps=="on" or newlineremover=="on" or extraspaceremover=="on" or stob=="on":

        return render(request, 'analyze.html', params)




    else:
        return HttpResponse("<h1>You Haven't Selected Any Operation</h1>")

