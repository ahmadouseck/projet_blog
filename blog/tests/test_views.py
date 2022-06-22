from django.forms import SlugField
from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home')
        self.detail_url = reverse('post_detail',args=['post1'])

        self.user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")

        self.post1 = Post.objects.create(
            title="post1",
            slug = "post1",
            author=self.user,
            updated_on="2022-06-21",
            content="lorem ipsum dolor sit amet",
            created_on="2022-06-19",
        )

    def test_list_posts(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')
        print("test_views1: OK")

    def test_detais_posts(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'post_detail.html')
        print("test_views2: OK")

