from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Item
from .forms import ItemForm

# Create your views here.
# 1. create your initial view. 
# 2. Import all the Items from Models, 
# 3. Save these items as the variable items, 
# 4. and then pass this variable to the html template in the context.

def classic_list(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }

    return render(request, "classic_list/classic_list.html", context)

def add_item(request):
    if request == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = ItemForm()
    context = {
        'form':form,
    }

    return render(request, "classic_list/add_item.html", context)