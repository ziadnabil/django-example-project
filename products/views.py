from django.db.models import query
from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product
from .forms import ProductModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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


# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 input_name = my_form.cleaned_data.get("name")
#                 Product.objects.create(name=input_name)
#             print("post_data", post_data)
#     return render(request, "forms.html", {})


@staff_member_required
def product_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        print(form.cleaned_data)
        data = form.cleaned_data
        Product.objects.create(**data)
        form = ProductModelForm()
        # return HttpResponseRedirect("")
        # return redirect("")
    return render(request, "forms.html", {"form": form})
