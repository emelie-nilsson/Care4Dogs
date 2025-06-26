from django import template

register = template.Library()

@register.filter
def cloud_crop(url, size='400x300'):
    if not url:
        return 'https://res.cloudinary.com/dsbygxnqw/image/upload/v1750936109/care4dogs/default.webp'
    try:
        w, h = size.split('x')
        return url.replace('/upload/', f'/upload/c_fill,g_auto,w_{w},h_{h}/')
    except Exception:
        return url