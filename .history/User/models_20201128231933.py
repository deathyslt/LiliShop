from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.phone}'


    def save(self, *args, **kwargs):
        if not self.phone:
            raise ValueError('Phone lazeme.')

        user_obj = User.objects.create(username=self.phone)
        self.user = user_obj
        return super(UserProfile, self).save(*args, **kwargs)
