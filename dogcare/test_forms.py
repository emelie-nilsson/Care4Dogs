from django.test import TestCase
from .forms import CommentForm
from .forms import DogCarePostForm

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'content': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())


class TestDogCarePostForm(TestCase):

    def test_valid_form(self):
        form = DogCarePostForm({
            'post_type': 'request',
            'title': 'Need help this weekend',
            'content': 'Looking for someone to care for my dog Lady',
            'location': 'Stockholm',
            'date_from': '2025-07-05',
            'date_to': '2025-07-07'
        })
        self.assertTrue(form.is_valid())

    def test_missing_title(self):
        form = DogCarePostForm({
            'post_type': 'offer',
            'title': '',
            'content': 'Happy to help with your dog',
            'location': 'Uppsala',
            'date_from': '2025-07-10',
            'date_to': '2025-07-12'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_missing_dates(self):
        form = DogCarePostForm({
            'post_type': 'request',
            'title': 'No dates given',
            'content': 'I forgot the dates!',
            'location': 'Lund',
            'date_from': '',
            'date_to': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date_from', form.errors)
        self.assertIn('date_to', form.errors)  

    def test_date_to_before_date_from(self):
        form = DogCarePostForm({
            'post_type': 'request',
            'title': 'Backwards dates',
            'content': 'This should not validate',
            'location': 'Göteborg',
            'date_from': '2025-07-10',
            'date_to': '2025-07-05'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date_to', form.errors)
        self.assertEqual(form.errors['date_to'], ["End date cannot be before start date."])          