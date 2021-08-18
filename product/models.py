from django.db import models


class FastFood(models.Model):
    title = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title
