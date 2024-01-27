from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HTMLAssetViewSet, ExtractedDataViewSet
from . import views 

router = DefaultRouter()
router.register(r'html_assets', HTMLAssetViewSet)
router.register(r'extracted_data', ExtractedDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index , name='index'),
]
