from django.db import models


class GalleryImages(models.Model):
    image = models.FileField()
    thumb = models.FileField()
