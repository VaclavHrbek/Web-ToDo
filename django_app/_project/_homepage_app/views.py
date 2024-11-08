from django.shortcuts import render

def index(request):
    return render(request, '_homepage_app/index.html')
