from django.db import models
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length = 3000, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images', blank = True)

    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
    def __str__ (self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts/:posts_detail", kwargs={"pk": self.pk})
    
    
class Comments(models.Model):
    commentaire = models.TextField(blank = True)
    like = models.BooleanField()
    post = models.ForeignKey(Posts, on_delete = models.CASCADE)
        
    class Meta:
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')
        
    def __str__ (self):
        return self.commentaire
    
    def get_absolute_url(self):
        return reverse("comments/:comments_detail", kwargs={"pk": self.pk})
