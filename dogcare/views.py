from django.shortcuts import render, redirect
from .models import DogCarePost
from .forms import DogCarePostForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = DogCarePost.objects.all()
    return render(request, 'dogcare/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = DogCarePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = DogCarePostForm()
    return render(request, 'dogcare/post_form.html', {'form': form})