from django.shortcuts import render
from .models import Items


# Create your views here.
def items_list(request):
    items = Items.objects.all()
    return render(request, 'core/items_list.html', {'items': items})