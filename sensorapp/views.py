from django.shortcuts import render


# Create your views here.
def welcome_view(request):
    return render(request, 'sensorapp/base.html')

