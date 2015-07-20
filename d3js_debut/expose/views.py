from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'expose/index.html') #does not have the context arg in this case
