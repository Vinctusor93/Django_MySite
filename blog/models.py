from django.db import models
from django.utils import timezone
from .validators import validate_year


class Profile(models.Model):
    name = models.CharField(max_length=30,primary_key = True)
    photo = models.ImageField(upload_to='pic_folder/profile/')
    description = models.TextField()

class Manga(models.Model):
        name = models.CharField(max_length=60,primary_key = True)
        author = models.CharField(max_length=30)
        genre = models.CharField(max_length=100)
        year_release = models.IntegerField(validators=[validate_year])
        photo = models.ImageField(upload_to='pic_folder/manga/')
        description = models.TextField()
        status_choice =(("Finished","Terminato"),("Ongoing", "In Corso"))
        status = models.CharField(max_length=20,choices = status_choice,default="In Corso")
        comment = (("Excellent","Molto bello"),("good","Buono"),("normal","Normale"),("bad","Brutto"),("very bad","Schifo"))
        vote = models.CharField(max_length=20,choices = comment,default="Normale")


class Game(models.Model):
        name = models.CharField(max_length=60,primary_key = True)
        genre = models.CharField(max_length=100)
        product_factory = models.CharField(max_length=60)
        year_release = models.IntegerField(validators=[validate_year])
        photo = models.ImageField(upload_to='pic_folder/games/')
        description = models.TextField()
        comment = (("Excellent","Molto bello"),("good","Buono"),("normal","Normale"),("bad","Brutto"),("very bad","Schifo"))
        vote = models.CharField(max_length=20,choices = comment,default="normale")

class Project(models.Model):
        name = models.CharField(max_length=30,primary_key = True)
        argument = models.CharField(max_length=60)
        group = models.CharField(max_length=60)
        tecnologies = models.CharField(max_length=60)
        photo = models.ImageField(upload_to='pic_folder/projects/')
        description = models.TextField()
