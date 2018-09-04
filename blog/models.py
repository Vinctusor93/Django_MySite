from django.db import models
from django.utils import timezone

#class Post(models.Model):
#    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#    title = models.CharField(max_length = 150)
#    text = models.TextField()
#    date_created = models.DateField(default=timezone.now())
#    date_published = models.DateField(default=timezone.now())
# Create your models here.

#def publish(self):
#    self.data_published = timezone.now()
#    self.save()


class Profile(models.Model):
    name = models.CharField(max_length=30,primary_key = True)
    photo = models.ImageField(upload_to='static/blog/pic_folder/profile/')
    description = models.TextField()

class Manga(models.Model):
        name = models.CharField(max_length=60,primary_key = True)
        author = models.CharField(max_length=30)
        genre = models.CharField(max_length=60)
        photo = models.ImageField(upload_to='static/blog/pic_folder/manga/')
        description = models.TextField()
        comment = (("Excellent","Molto bello"),("good","buono"),("normal","normale"),("bad","brutto"),("very bad","schifo"))
        vote = models.CharField(max_length=20,choices = comment,default="normale")


class Game(models.Model):
        name = models.CharField(max_length=30,primary_key = True)
        genre = models.CharField(max_length=60)
        product_factory = models.CharField(max_length=60)
        photo = models.ImageField(upload_to='static/blog/pic_folder/games/')
        description = models.TextField()
        comment = (("Excellent","Molto bello"),("good","buono"),("normal","normale"),("bad","brutto"),("very bad","schifo"))
        vote = models.CharField(max_length=20,choices = comment,default="normale")

class Project(models.Model):
        name = models.CharField(max_length=30,primary_key = True)
        argument = models.CharField(max_length=60)
        group = models.CharField(max_length=60)
        tecnologies = models.CharField(max_length=60)
        photo = models.ImageField(upload_to='static/blog/pic_folder/projects/')
        description = models.TextField()
