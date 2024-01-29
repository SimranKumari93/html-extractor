from django.db import models

class HTMLAsset(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

class ExtractedData(models.Model):
    asset = models.ForeignKey(HTMLAsset, on_delete=models.CASCADE)
    data = models.TextField()
