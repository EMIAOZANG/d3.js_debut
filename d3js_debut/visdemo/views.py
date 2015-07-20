from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'visdemo/index.html')

def svg_demo(request):
    return render(request, 'visdemo/svg.html')
