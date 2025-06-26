from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DogCarePost
from .forms import DogCarePostForm

def post_list(request):
    posts = DogCarePost.objects.all()
    return render(request, 'dogcare/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(DogCarePost, id=post_id)
    # Här kan du senare lägga till kommentarsfunktioner
    return render(request, 'dogcare/post_detail.html', {'post': post})

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

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(DogCarePost, id=post_id, user=request.user)
    if request.method == 'POST':
        form = DogCarePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = DogCarePostForm(instance=post)
    return render(request, 'dogcare/post_form.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(DogCarePost, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'dogcare/post_confirm_delete.html', {'post': post})