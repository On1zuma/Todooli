import os
import random
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

import os
from uuid import uuid4

from Inotki import settings


def path_and_rename(path):
    # Rename users pictures
    def wrapper(instance, filename):

        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            # if i want to put the id on the name
            # filename = '{}.{}'.format(instance.pk, ext)
            filename = '{}_{}.{}'.format(instance.pk, uuid4().hex, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file

        return os.path.join(path, filename)

    # Sometimes this wrapper can cause an error during migration; comment it out to complete the migration.
    return wrapper


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(default=f'{settings.MEDIA_ROOT}/profile_pics/default.jpg',
                              null=False,
                              blank=False,
                              upload_to=path_and_rename('profile_pics'))

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        # Delete previous image
        try:
            this = Profile.objects.get(id=self.id)
            if this.image != self.image and this.image != f'{settings.MEDIA_ROOT}/profile_pics/default.jpg':
                this.image.delete()
        except:
            pass

        # We crop the image (image reformatting)
        super().save()

        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)
