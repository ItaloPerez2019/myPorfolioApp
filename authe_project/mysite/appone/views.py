from django.shortcuts import render,redirect

# Create your views here.
def appones (request):
    return render(request,'appone/hometwo.html',{})

def count (request):
    fulltext=request.GET['fulltext']
    wordlist = fulltext.split()


    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase: 
            worddictionary[word] +=1

        else:
            #add to dict
            worddictionary[word] =1



    return render(request,'appone/count.html',{'fulltext': fulltext, 'count':len(wordlist), 'worddictionary': worddictionary.items() })
