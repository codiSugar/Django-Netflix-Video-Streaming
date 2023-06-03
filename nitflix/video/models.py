from django.db import models

# Create your models here.




class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    video_id = models.CharField(max_length=10)
    # timestamp
    # updated
    # state
    
    
    
    
# netflix 123