from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Communautes(models.Model):
    noms = models.TextField()
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return str(self.noms)


class Priorite(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return str(self.label)


class Post(models.Model):
    titre = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=100)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    communaute = models.ForeignKey(Communautes, related_name='communaute', on_delete=models.CASCADE)
    priorite = models.ForeignKey(Priorite, related_name='priorite', null=True, on_delete=models.CASCADE)
    evenementiel = models.BooleanField(default=False)
    date_evenement = models.DateField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='auteur', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titre)


class Commentaire(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    contenu = models.CharField(max_length=300)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contenu)
