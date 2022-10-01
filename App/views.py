from dataclasses import replace
from django.shortcuts import render
from django.shortcuts import HttpResponse,render

def index(request):
    return render(request,"index.html")


def analyzer(request):
    djtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc",'off')
    fullcaps=request.POST.get("uppercase",'off')
    oneline=request.POST.get("singleline",'off')
    spaceremover=request.POST.get("sapceremove",'off')




    if removepunc=="on":

        punctuations=""".?!:;—( )[ ]{ }< >“ ”‘/… *&~\@^|"""
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+ char
            
        
        context={"analize":"your analyzed text- Removed Punctuation",'analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        context={"analize":"your analyzed text-chage to uppercase",'analyzed_text':analyzed}
        djtext=analyzed
    


    if(oneline=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        context={"analize":"your analyzed text-Remove new line",'analyzed_text':analyzed}
        djtext=analyzed


    if(spaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed=analyzed+char
        context={"analize":"your analyzed text-Remove Space",'analyzed_text':analyzed}
        djtext=analyzed



        
    if removepunc!="on" and fullcaps!="on" and oneline!="on" and spaceremover!="on":
            return HttpResponse("Please select one option error")


    return render(request,"analyze.html",context)




def aboutus(request):
    return render(request,"Aboutus.html") 

def contactus(request):
    return render(request,"contactus.html")









"""def capitalizefirst(request):
    return HttpResponse("here capitalizefirst")


def newlineremove(request):
    return HttpResponse("here newlineremove")


def spaceremove(request):
    return HttpResponse("here spaceremove")



def charcount(request):
    return HttpResponse("here charcount") """