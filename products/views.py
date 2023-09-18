from django.shortcuts import render
from django.http import HttpResponse

from .models import Products

# Create your views here.
def index(request):
    productsLists = Products.objects.all()

    context = {
        'title' : 'Crud Django',
        'lists' : productsLists
    }
    return render(request, "products/index.html", context)

def about(request):
    return render(request, "products/about.html")


def task_detail(request, id):
    Productslist = Products.objects.get(id=id)

    context = {
        'title': Productslist.title,
        'list': Productslist
    }

    return render(request, "products/details.html", context)
