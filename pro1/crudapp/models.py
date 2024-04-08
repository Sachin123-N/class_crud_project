from django.db import models


class Book(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mob_no = models.IntegerField()



