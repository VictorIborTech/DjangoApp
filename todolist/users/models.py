from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    address = models.TextField(blank=True, max_length=200)
    interest = models.TextField(max_length=300,blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        default='avatar.jpg',  # default avatar
        upload_to='profile_avatars'  # dir to store the image
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height >300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)