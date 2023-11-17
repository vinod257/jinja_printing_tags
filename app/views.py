from django.shortcuts import render

# Create your views here.

def vinod(request):
    data='i need a job'
    d={'job':data} 
    return render(request,'vinod.html',context=d)
def v1(request):
    d={'username':'isha','age':25,'place':'anantapur'}
    return render(request,'v1.html',context=d)
