from django.shortcuts import render, get_object_or_404

from . models import GalleryImages


def index(request):
    from django.conf import settings
    import os
    media_dir = settings.MEDIA_ROOT
    thumb_folder = os.path.join(media_dir, 'thumbs')
    thumbs = [thumb for thumb in os.scandir(thumb_folder)]
    return render(request, 'gallery/index.html', {'thumbs': thumbs})
