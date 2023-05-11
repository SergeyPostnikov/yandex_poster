from django.db import models
from tinymce.models import HTMLField


class Image(models.Model):
    img = models.ImageField(blank=True, null=True)
    place = models.ForeignKey(
            'Place', 
            related_name='images', 
            on_delete=models.CASCADE
        )
    order_num = models.IntegerField(blank=True, null=True, default=1)

    class Meta:
        ordering = ['order_num']

    def __str__(self):
        return f'{self.order_num}-{self.place.__str__()}'


class Place(models.Model):
    title = models.CharField(max_length=40)
    description_short = models.TextField(
        blank=True, 
        null=True
    )
    description_long = HTMLField(blank=True, null=True)
    lon = models.FloatField(
        null=True,
        verbose_name='Longitude'
        )
    lat = models.FloatField(
        null=True,
        verbose_name='Latitude'
        )

    def __str__(self):
        return f'{self.title}'
