from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

from common.resize_image import resize_image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/user/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        img = self.image
        if img:
            size = 300, 300
            quality = 75
            upload_to = 'images/user/%Y/%m/%d/'
            self.image = resize_image(img, size, quality, upload_to)
        super().save(*args, **kwargs)
