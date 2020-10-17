from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product

# Create your views here.
def home(request, *args, **kwargs):
    context = {"name": "home"}
    return render(request, "home.html", context)


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f"Product id : {obj.id}")


def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"ALert": "product not found"})
    return JsonResponse({"id": obj.id})
