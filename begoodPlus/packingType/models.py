from django.db import models

# Create your models here.
class PackingType(models.Model):
    name = models.CharField(verbose_name='packing type', max_length=50)

    def __str__(self):
        return self.name
    