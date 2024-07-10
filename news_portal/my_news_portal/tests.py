from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *
from .forms import *


class TestMyNewsPortal(APITestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(name='Спорт')
        self.category_2 = Category.objects.create(name='Наука')
        self.user_1 = User.objects.create(username='JohnDoe')
        self.author_1 = Author.objects.create(user=self.user_1)
        self.post_1 = Post.objects.create(author=self.author_1, type='NE', title='t', text='t')
        self.comment_1 = Comment.objects.create(post=self.post_1, user=self.user_1, text='t')

    def test_list_posts_view(self):
        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_post_view(self):
        response = self.client.get(reverse('detail_post', args=[self.post_1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_form(self):
        all_categories = Category.objects.all()
        data = {'author': self.author_1, 'categories': all_categories, 'title': 'test_title', 'text': 'test_text'}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_comment_form(self):
        data = {'text': 'random_text'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_create_news_view(self):
        response = self.client.get(reverse('create_news'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_create_article_view(self):
        response = self.client.get(reverse('create_article'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_post_view(self):
        response = self.client.get(reverse('edit_post', args=[self.post_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_post_view(self):
        response = self.client.get(reverse('delete_post', args=[self.post_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_like_post(self):
        response = self.client.post(reverse('like_post', args=[self.post_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_dislike_post(self):
        response = self.client.post(reverse('dislike_post', args=[self.post_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_subscribe_to_category(self):
        response = self.client.post(reverse('subscribe_to_category', args=[self.category_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_unsubscribe_from_category(self):
        response = self.client.post(reverse('unsubscribe_to_category', args=[self.category_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_create_comment_view(self):
        response = self.client.get(reverse('create_comment'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_comment_view(self):
        response = self.client.get(reverse('edit_comment', args=[self.comment_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_comment_view(self):
        response = self.client.get(reverse('delete_comment', args=[self.comment_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_like_comment(self):
        response = self.client.post(reverse('like_comment', args=[self.comment_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_dislike_comment(self):
        response = self.client.post(reverse('dislike_comment', args=[self.comment_1.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
