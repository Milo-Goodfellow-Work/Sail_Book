from django.db import models
import datetime
import secrets


# Create your models here.
class listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField(
                        max_length=300,
                        blank=False,
                        null=False)
    price = models.IntegerField()
    email = models.CharField(max_length=300)
    image_one = models.ImageField(
                        upload_to='images/',
                        height_field=None,
                        width_field=None,
                        max_length=100)
    image_two = models.ImageField(
                        upload_to='images/',
                        height_field=None,
                        width_field=None,
                        max_length=100)
    image_three = models.ImageField(
                        upload_to='images/',
                        height_field=None,
                        width_field=None,
                        max_length=100)
    public_token = models.CharField(
                        max_length=200,
                        default=secrets.token_urlsafe(22))
    secret_token = models.CharField(
                        max_length=200,
                        default=secrets.token_urlsafe(22))
    creation_date = models.DateField(default=datetime.date.today)
