from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # from Pillow to resize the image before saving it


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # added *args , **kwargs in Part 13
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # to override the direct save

        # this will open the image of the current instance
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)    # max_dimensions allowed
            img.thumbnail(output_size)  # create a thumbnail with that size
            img.save(self.image.path)   # overwrite the original image

            # NOTE: There are packages that can do this
