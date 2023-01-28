"""new_dawn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # adding alluath urls to project level file
    path('accounts/', include('allauth.urls')),
    # adding homepage urls to project level file
    path('', include('homepage.urls')),
    # adding products urls to project level file
    path('products/', include('products.urls')),
    # adding shoppingbag urls to project level file
    path('shoppingbag/', include('shoppingbag.urls')),
    # adding checkout urls to project level file
    path('checkout/', include('checkout.urls')),
    # adding profile urls to project level file
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#using static function to add url to media urls