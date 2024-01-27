from rest_framework import viewsets
from .models import HTMLAsset, ExtractedData
from .serializers import HTMLAssetSerializer, ExtractedDataSerializer
from django.http import HttpResponse 
def index(request):
    return HttpResponse("Welcome to the data extraction system!")


class HTMLAssetViewSet(viewsets.ModelViewSet):
    queryset = HTMLAsset.objects.all()
    serializer_class = HTMLAssetSerializer

class ExtractedDataViewSet(viewsets.ModelViewSet):
    queryset = ExtractedData.objects.all()
    serializer_class = ExtractedDataSerializer
