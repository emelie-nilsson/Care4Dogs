from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  
from django.utils.timezone import now

"""
A model to create and manage requests of dogcare
"""

class DogCarePost(models.Model):
    POST_TYPE_CHOICES = [
        ('request', 'Needs Dog Care'),
        ('offer', 'Can Offer Dog Care'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES)
    location = models.CharField(max_length=100, blank=True)
    date_from = models.DateField(null=False, blank=False)
    date_to = models.DateField(null=False, blank=False)
    image = CloudinaryField('image', blank=True, null=True, default='care4dogs/default')  
    date_posted = models.DateTimeField(auto_now_add=True)  
    last_updated = models.DateTimeField(auto_now=True) 

    # Likes
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.title} ({self.get_post_type_display()})"
    
class Comment(models.Model):  
    post = models.ForeignKey(DogCarePost, on_delete=models.CASCADE, related_name='comments')  # NYTT
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"Comment by {self.user.username} on {self.post.title}"