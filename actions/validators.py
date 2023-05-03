from photos.models import Image


def is_favorite(product_url: str) -> bool:
    return len(Image.objects.filter(url=product_url)) > 0
