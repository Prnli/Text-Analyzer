#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request) :
    #return HttpResponse("<h1>Home</h1>")  #---> for returning a plane response without html template
    #return render(request, 'home.html')
    return render(request, 'homewithbootstrap.html')

def remove_punc(request) :
    return HttpResponse("<h1>Removed Punctuation</h1><a href='/'>back</a>")


#For Analyzing text
def analyze(request) :
    #for getting text
    djtext = request.POST.get('text','default')
    
    #to check for checkbox
    removepunc = request.POST.get('removepunc','off')
    caps = request.POST.get('caps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    
    #for printing on terminal
    print(removepunc)
    print(djtext)
    print(caps)
    
    if removepunc == "on" :
        punct = ''',.<>?/:;"'{}[]|\`~!@#$%^&*()_+-='''
        analyzed = ""
        for char in djtext :
            if char not in punct :
                analyzed = analyzed + char
        params = {'purpose':'removed punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    
    if caps=="on" :
        analyzed = ""
        for char in djtext :
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    
    if newlineremover=="on" :
        analyzed=""
        for char in djtext :
            if char !="\n" and char !="\r" :
                analyzed = analyzed + char
        params = {'purpose' : 'Extra line is removed', 'analyzed_text' : analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    if extraspaceremover=="on" :
        analyzed = ""
        for index,char in enumerate(djtext) :
            if(djtext[index] == " " and djtext[index+1] == " ") :
                pass
            else :
                analyzed = analyzed + char
        params = {'purpose' : 'Extra space is removed', 'analyzed_text' : analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    
    if charcounter=="on" :
        analyzed = ""
        count = 0
        for char in djtext :
            if char == " " :
                pass
            else :
                count+=1
        params = {'purpose' : 'Total characters is calculated', 'analyzed_text' : count}
        #return render(request,'analyze.html',params)
    
    if (removepunc !="on" and caps != "on" and newlineremover !="on" and extraspaceremover != "on" and charcounter != "on") :
        return HttpResponse('''<h2 style="color:red;">Please provide valid input !!!</h2>''')
    
    return render(request,'analyze.html',params)

    
#For navigation on diff site
def nav(request) :
    sites = '''<h1><a href="https://www.google.com">Google</a></h1>'''
    return HttpResponse(sites)