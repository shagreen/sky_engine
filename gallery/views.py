import base64
from django.shortcuts import render, redirect, get_object_or_404
from .service import GalleryService
from .models import GalleryImage


def gallery_preview(request):
    image_bytes = GalleryService.fetch_image_bytes()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    if request.method == "POST":
        index = request.POST.get("index")
        if index and index.isdigit():
            GalleryService.save_image(int(index))
            return redirect(f"/gallery/preview/{index}/")
    elif request.method == "GET":
        GalleryService.save_temp_image(image_bytes)

    return render(request, "gallery/preview.html", {"image_base64": image_base64})


def gallery_index(request, index):
    obj = get_object_or_404(GalleryImage, index=index)
    return render(request, "gallery/index.html", {"image_url": obj.image.url})
