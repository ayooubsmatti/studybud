from django.shortcuts import render


rooms= [
    {'id':1,'name':'Lets learn python!'},
    {'id':2,'name':'Lets devoloper'},
    {'id':3,'name':'Lets learn css!'},
]
# Create your views here.
def home(request):
    return render(request, 'base/home.html')
def room(request):
    context = {'rooms':rooms}
    return render(request, 'base/room.html',context)