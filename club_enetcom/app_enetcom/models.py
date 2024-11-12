from django.db import models
from django.contrib.auth.models import User,Permission,AbstractUser

# Create your models here.
class Etudianti(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    Numero= models.IntegerField()

class Clubi(models.Model):
    nom = models.CharField(max_length=100)
    membres = models.ManyToManyField(Etudianti, through='MembreClubi')
    
    def __str__(self):
        return self.nom

class PresidentClubi(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    etudi = models.OneToOneField(Etudianti, on_delete=models.CASCADE)
    Club=models.OneToOneField(Clubi,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    Numero= models.IntegerField()

    class Meta:
      permissions = [
        ("can_add_membre", "Can add les membres"),
    ]
   
    
class MembreClubi(models.Model):
    etud = models.ForeignKey(Etudianti, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubi, on_delete=models.CASCADE)

from django.conf import settings
class Messages(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(Clubi, on_delete=models.CASCADE, related_name='received_messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')

class actualite(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    club=models.ForeignKey(Clubi,on_delete=models.CASCADE)

