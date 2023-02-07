from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Items

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)

    return render(request, "item/detail.html", {"item": item})
