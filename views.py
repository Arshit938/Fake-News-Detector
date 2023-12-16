from django.http import HttpResponse
from django.shortcuts import render
from detector import stemming,detect

def index(request):
    return render(request,'index.html')

def predict(request):
    return render(request,'prediction.html')

def detection(request):
    author=request.GET.get('author')
    news=request.GET.get('title')

    query=author+' '+news
    st=stemming(query)
    if detect(st):
        ans='Real'
        status='success'
    else:
        ans='Fake'
        status='danger'
    x={'ans':ans,'status':status}
    return render(request,'answer.html',x)




