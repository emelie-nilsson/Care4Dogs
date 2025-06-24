from django.shortcuts import render
from .models import DogCarePost

def post_list(request):
    posts = DogCarePost.objects.all()
    return render(request, 'dogcare/post_list.html', {'posts': posts})