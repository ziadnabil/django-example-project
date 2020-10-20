from django.db.models import query
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product


""" def ordinary_view(request, *args, **kwargs):
    my_request_data = dict(request.GET)
    new_product = my_request_data.get("new_product")
    print(my_request_data, new_product)
    if new_product[0].lower() == "true":
        print("new_product")
        Product.objects.create(
            name=my_request_data.get("name"),
            price=my_request_data.get("price"),
        )
    return HttpResponse("ordinary") """


def search_view(request, *args, **kwargs):
    query = request.GET.get("q")
    qs = Product.objects.filter(name__icontains=query[0])
    print(query, qs)
    context = {"name": "home", "query": query}
    return render(request, "home.html", context)


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id : {obj.id}")
    return render(request, "products/detail.html", {"object": obj})


def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"ALert": "product not found"})
    return JsonResponse({"id": obj.id})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


def product_create_view(request):
    print(request.POST)
    print(request.GET)
    return render(request, "forms.html", {})
