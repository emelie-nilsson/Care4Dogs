from django.core.files.uploadedfile import SimpleUploadedFile

def setUp(self):
    self.user = User.objects.create_user(username='viewuser', password='testpass')

    # Create an emty image file for testing
    test_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=b'',  
        content_type='image/jpeg'
    )

    self.post = DogCarePost.objects.create(
        user=self.user,
        title='Dog sitting needed',
        content='Can anyone help?',
        post_type='request',
        location='Stockholm',
        date_from=date(2025, 7, 1),
        date_to=date(2025, 7, 3),
        image=test_image  
    )
