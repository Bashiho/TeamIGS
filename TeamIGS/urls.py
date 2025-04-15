"""
URL configuration for TeamIGS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import (
    # IndexView,
    DetailView,
    index,
    cart,
    checkout,
    updateItem,
    processOrder,
)
from . import views

from django.conf.urls.static import static 
from django.conf import settings

app_name = "TeamIGS"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("updateItem/", updateItem, name="updateItem"),
    path("processOrder/", processOrder, name="processOrder")
    
    # Not implemented yet
    # Page containing list of categories, not working
    # path("category/", InCategoryView.as_view(), name="category"),
    # Page containing items within category
    # path("category/<str:name>/", InCategoryView.as_view(), name="inCategory"),
    path("category/<str:name>/", InCategoryView.as_view(), name="inCategory"),
    # Currently placeholder, requires login.html to be made
    path("login/", loginView.as_view(), name="login"),
    # Css testing page:
    path("csstest/", views.csstest)
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
