from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('images', views.ImagesViewSet, basename='images')
router.register('collections', views.CollectionViewSet, basename='collections')

urlpatterns = router.urls
