from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Index\index.html')

def Prepare(request):
    return render(request, 'Index\prepare.html')