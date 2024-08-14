from django.db import models


class Pc(models.Model):
    id = models.CharField(max_length=5, primary_key=True,  unique=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    classroom = models.IntegerField()
    ssd = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pc"
        verbose_name_plural = 'Pcs'

    def __str__(self):
        return self.id
