from django.test import TestCase
from .models import Video
# Create your tests here.




class VideoModelTest(TestCase):
    def setUp(self):
        Video.objects.create(title = 'Betal Season 1')
        
    def test_valid_title(self):
        title = 'Betal Season 1'
        qs = Video.objects.filter(title = title)
        self.assertTrue(qs.exists()) 