# Generated by Django 2.2.8 on 2021-05-24 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Communautes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noms', models.TextField()),
                ('abonnes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_de_creation', models.DateTimeField()),
                ('evenement', models.BooleanField(default=False)),
                ('date_evenement', models.DateField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to=settings.AUTH_USER_MODEL)),
                ('communaute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communaute', to='communitymanager.Communautes')),
            ],
        ),
    ]
