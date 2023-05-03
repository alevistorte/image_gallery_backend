
from django.urls import path
from .views import save_product, get_product_photos, searching_from_CGT

urlpatterns = [
    path('saveItem/', save_product, name='my-view'),
    path('getProductPhotos/', get_product_photos, name='get-photos'),
    path('search/', searching_from_CGT, name='search')
]
