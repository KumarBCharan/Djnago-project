from django.shortcuts import render

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')
'''def home(request):
    return render(request,'home.html')'''
def alerts(request):
    return render(request,'alerts.html')
def buttons(request):
    return render(request,'buttons.html')

def badge(request):
    return render(request,'badge.html')

def forms(request):
    return render(request,'forms.html')
def dropdown(request):
    return render(request,'dropdown.html')


def buttongroup(request):
     return render(request,'buttongroup.html')
