from django.db import models

from django.contrib.auth.models import AbstractUser

from patron.models import Patron


class Creator(AbstractUser):
    subscribers = models.ForeignKey(
        Patron, related_name="patrons", on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="images/", default="images/default-profile-picture.png"
    )
    email = models.EmailField(max_length=50)
