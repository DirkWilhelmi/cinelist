from django.shortcuts import render
from cinelist.models import Cinema

# Create your views here.
def index(request):
    cinemalist = Cinema.objects.order_by('name')
    is_this_true = True
    context = {'cinemalist': cinemalist,
               'is_this_true': is_this_true}
    return render(request, 'cinelist/index.html', context)