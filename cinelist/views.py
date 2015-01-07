from django.shortcuts import render
from cinelist.models import Cinema

# Create your views here.
def index(request):
    cinemalist = Cinema.objects.order_by('name')
    context = {'cinemalist': cinemalist}
    return render(request, 'cinelist/index.html', context)