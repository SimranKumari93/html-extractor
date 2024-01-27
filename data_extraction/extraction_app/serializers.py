from rest_framework import serializers
from .models import HTMLAsset, ExtractedData

class HTMLAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTMLAsset
        fields = '__all__'

class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = '__all__'
