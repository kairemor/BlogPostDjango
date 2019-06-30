from email.policy import default

from django.contrib.auth.models import User
from django.db import models


SEXE = (
    ('M', 'Masculin'),
    ('F', 'Feminin'),
)

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='')
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=50, default='')
    job = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile', blank=True)
    sexe = models.CharField(max_length=2,  choices=SEXE, default='')

    def __str__(self):
        return self.user.username
