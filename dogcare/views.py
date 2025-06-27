from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DogCarePost, Comment  # NYTT: Importera Comment
from .forms import DogCarePostForm, CommentForm  # NYTT: Importera CommentForm

def post_list(request):
    posts = DogCarePost.objects.all()
    return render(request, 'dogcare/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(DogCarePost, id=post_id)
    comments = post.comments.all().order_by('-created_at')  # NYTT: Hämta kommentarer sorterade senaste först

    liked = False
    total_likes = post.likes.count()

    if request.user.is_authenticated:
        liked = post.likes.filter(id=request.user.id).exists()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,  
        'liked': liked,
        'total_likes': total_likes,
        'form': form,  
    }
    return render(request, 'dogcare/post_detail.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = DogCarePostForm(request.POST, request.FILES)  
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
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
            return redirect('post_detail', post_id=post.id)
    else:
        form = DogCarePostForm(instance=post)
    return render(request, 'dogcare/post_form.html', {'form': form, 'post': post})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(DogCarePost, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'dogcare/post_confirm_delete.html', {'post': post})

@login_required
def toggle_like(request, pk):
    post = get_object_or_404(DogCarePost, pk=pk)
    user = request.user
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('post_detail', pk=pk)