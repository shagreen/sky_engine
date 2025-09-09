from django.db import models


class GalleryImage(models.Model):
    index = models.PositiveIntegerField(primary_key=True)
    image = models.ImageField(upload_to="gallery/images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"GalleryImage(index={self.index})"


class GalleryTempImage(models.Model):
    image = models.ImageField(upload_to="gallery/images/")
    # TODO: User?

    def __str__(self):
        return f"GalleryTempImage"
