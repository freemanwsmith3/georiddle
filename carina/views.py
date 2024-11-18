from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Content

def get_content(request, code):
    content = get_object_or_404(Content, code=code)
    data = {
        'id': content.id,
        'image_url': content.image_url,
        'title': content.title,
        'description': content.description,
        'link': content.link
    }
    return JsonResponse(data)