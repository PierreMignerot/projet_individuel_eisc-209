from django import forms
from .models import Commentaire, Post


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=30)
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)


class CreatepostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('communaute', 'titre', 'description', 'evenementiel', 'date_evenement', 'priorite')


class ModifpostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('communaute', 'titre', 'description', 'evenementiel', 'date_evenement', 'priorite')
