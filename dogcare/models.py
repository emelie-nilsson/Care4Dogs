from django.db import models
from django.contrib.auth.models import User

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
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='dogcare_images/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.title} ({self.get_post_type_display()})"