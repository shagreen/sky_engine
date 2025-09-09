import requests
from django.core.files.base import ContentFile
from .models import GalleryImage, GalleryTempImage


class GalleryService:
    BASE_URL = "https://thispersondoesnotexist.com/"

    @staticmethod
    def fetch_image_bytes():
        resp = requests.get(GalleryService.BASE_URL, timeout=15)
        resp.raise_for_status()
        return resp.content

    @staticmethod
    def save_image(index):
        obj, created = GalleryImage.objects.get_or_create(index=index)
        filename = f"index_{index}.jpg"
        obj.image.save(
            filename,
            ContentFile(GalleryTempImage.objects.first().image.read()),
            save=True,
        )
        return obj

    @staticmethod
    def save_temp_image(image_bytes):
        obj, created = GalleryTempImage.objects.get_or_create(id=1)
        filename = f"temp.jpg"
        obj.image.save(filename, ContentFile(image_bytes), save=True)
        return obj
