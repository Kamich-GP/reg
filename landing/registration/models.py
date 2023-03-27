from django.db import models

# Create your models here.


class Captain(models.Model):
    name_surname = models.CharField(max_length=128, null=True)
    pro_potok = models.CharField(max_length=256, null=True)

    name_surname1 = models.CharField(max_length=128, null=True)
    pro_potok1 = models.CharField(max_length=256, null=True)
    name_surname2 = models.CharField(max_length=128, null=True)
    pro_potok2 = models.CharField(max_length=256, null=True)
    name_surname3 = models.CharField(max_length=128, null=True)
    pro_potok3 = models.CharField(max_length=256, null=True)
    name_surname4 = models.CharField(max_length=128, null=True)
    pro_potok4 = models.CharField(max_length=256, null=True)
    name_surname5 = models.CharField(max_length=128, null=True)
    pro_potok5 = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name







