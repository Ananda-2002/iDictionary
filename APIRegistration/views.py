from django.shortcuts import render

# Create your views here.


def api_registration(request):
    return render(request, 'api_registration.html')
