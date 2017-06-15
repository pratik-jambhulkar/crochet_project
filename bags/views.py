from django.shortcuts import render
from bags.models import Category


def home_page(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
