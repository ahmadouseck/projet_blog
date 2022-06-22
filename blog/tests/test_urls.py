from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import PostList,PostDetail

class TestsUrls(SimpleTestCase):
    def test_list_urls(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)
        print("test_urls1: OK")
    
    def test_detail_urls(self):
        url = reverse('post_detail',args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail) 
        print("test_urls2: OK")
