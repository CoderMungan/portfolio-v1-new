from django.db import models

# Create your models here.



class Animal(models.Model):
    name = models.CharField(("Name Animal"), max_length=50)
    width = models.IntegerField(("Animal Width"))
    height = models.IntegerField(("Animal Height"))
    tur = models.CharField(max_length=50)
    yas = models.IntegerField()
    renk = models.CharField(max_length=50, blank=True, null=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name