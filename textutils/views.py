#i have created this file - yo
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

# 1 #
# def index(request):
#     return HttpResponse("hello")

# def about(request):
#     return HttpResponse(" about harry bhai ")

# 2 #
# def index(request):
#     prams={'name':'harry','place':'usa'}
#     return  render(request,'index.html',prams) #render is use when you want html file to display output rather than HttpResponse with this we use 
#     #return HttpResponse("home")               #html file to dispaly output render(1,2,3) 1,2 are complusory 3 is dictonary its your own wish you want
#                                                #to add or not   2 is html file name  

# 3 #
def index(request):
    return  render(request,'index.html')     

def analyze(request):
    #get the text analysis the text
    djtext=request.POST.get('text','default')
    #check value of checkbox
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    
    # print(removepunc)
    # print(djtext)
    
    #check which checkbox is on
    
    if removepunc=="on":
        pucations=""" ! () - [] {} ; : \ , <> . / ? @ # $ % ^ & * _ ~ """
        analyzed=""
        for char in djtext:
          if char not in pucations:
                analyzed=analyzed+char
        prams={'purpose':'remove puncations','analyzed_text':analyzed}
        # return render(request,'analyze.html',prams)
        djtext=analyzed 
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        prams={'purpose':'change to uppercase','analyzed_text':analyzed}
        # return render(request,'analyze.html',prams)    
        djtext=analyzed 
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
             analyzed=analyzed+char
        prams={'purpose':'newlineremover','analyzed_text':analyzed}
        # return render(request,'analyze.html',prams) 
        djtext=analyzed 
    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
              analyzed=analyzed+char
        prams={'purpose':'removeextraspace','analyzed_text':analyzed}
        # return render(request,'analyze.html',prams)  
        djtext=analyzed 
    if(charcounter=="on"):
        a=len(str(djtext))
        analyzed=f" The number of characters in text is {a}"
        prams={'purpose':'charcounter','analyzed_text':analyzed}
        # return render(request,'analyze.html',prams)  
                 
    if(removepunc!="on" and charcounter!="on" and extraspaceremover!="on" and newlineremover!="on" and  fullcaps!="on"):
        return HttpResponse("ERROR")

    return render(request,'analyze.html',prams)                                        
# def removepunc(request):
#     #get the text analysis the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("RENOVE PUNC")

# def capfirst(request):
#     return HttpResponse("capatilize first")

# def newlineremove(request):
#     return HttpResponse("capatilize first")

# def spaceremove(request):
#     return HttpResponse("capatilize first <a href='/'>back</a>") #this give option to move back to home page 

# def charcount(request):
#     return HttpResponse("capatilize first")

# def ex1(request):
#     s=''' Navigation Bar <br> </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>
#     reutrn HttpResponse(s)'''