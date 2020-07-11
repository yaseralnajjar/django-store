from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def home(request):
    return redirect('product_list')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('', include('products.urls')),
    path('', include('accounts.urls')),
    path('', include('carts.urls')),
    path('', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
