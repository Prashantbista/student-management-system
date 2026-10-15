from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def about(request):
    # return HttpResponse ("hello!")
    context={
        'titile':"prashant",
        'header':"Django",
        'paragraph':["this is first","this is second"]
    }
    return render(request,"aboutus/about.html",context)