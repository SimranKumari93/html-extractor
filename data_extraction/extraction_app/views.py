from rest_framework import viewsets
from .models import HTMLAsset, ExtractedData
from .serializers import HTMLAssetSerializer, ExtractedDataSerializer
from django.http import HttpResponse , JsonResponse
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, render
import requests
from .forms import MyForm

def index(request):
    return HttpResponse("Welcome to the data extraction system!")
def extract_data(request, asset_id):
    asset_id = get_object_or_404(HTMLAsset, pk=asset_id)
    response = requests.get(asset_id.url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract data using Beautiful Soup
        # Example: Extracting all text content from <p> tags
        paragraphs = [p.get_text() for p in soup.find.all('p')]
        # Save extracted data to the database
        extract_data = ExtractedData.objects.create(asset=asset, data='\n'.join(paragraphs))
        return JsonResponse({'success' : True, 'message' :' Data extracted Successfully'})
    else:
        return JsonResponse({'success': False, 'message' : 'Failed to extract html data'})

class HTMLAssetViewSet(viewsets.ModelViewSet):
    queryset = HTMLAsset.objects.all()
    serializer_class = HTMLAssetSerializer

class ExtractedDataViewSet(viewsets.ModelViewSet):
    queryset = ExtractedData.objects.all()
    serializer_class = ExtractedDataSerializer

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            # Add logic here to handle form submission
            print('Form submitted with value:', input_text)
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
