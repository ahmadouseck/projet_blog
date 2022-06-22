from django.test import TestCase
from requests import request
from blog.models import Post
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
         #Set up non-modified objects used by all test methods
        self.user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
       
        self.post = Post.objects.create(
            title="Mon titre",
            author= self.user,
            updated_on="2022-06-21",
            content="lorem ipsum dolor sit amet",
            created_on="2022-06-19",
        )
    def test_Postslugcreation(self):
        self.assertEquals(self.post.title, 'Mon titre')
        print("test_model1: OK")
    
    def test_post_is_posted(self):
        """Posts are created"""
        post1 = Post.objects.get(title="Mon titre")
        self.assertEqual(post1.content, "lorem ipsum dolor sit amet")
        print("test_model2: OK")

    
