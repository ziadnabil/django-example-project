"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path

from accounts.views import login_view, logout_view, register_view

from products.views import (
    product_detail_view,
    product_api_detail_view,
    search_view,
    product_list_view,
    product_create_view,
)

urlpatterns = [
    # path("ordinary_view/", ordinary_view),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
    path("login/", login_view),
    path("products-create/", product_create_view),
    path("products/", product_list_view),
    path("products/<int:pk>/", product_detail_view),
    path("api/products/<int:pk>/", product_api_detail_view),
    path("admin/", admin.site.urls),
    path("search/", search_view),
]
