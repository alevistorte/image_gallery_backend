
from django.urls import path
from .views import my_view, get_product_photos

urlpatterns = [
    path('saveItem/', my_view, name='my-view'),
    path('getProductPhotos/', get_product_photos, name='get-photos'),
]
