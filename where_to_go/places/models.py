from django.db import models


class Image(models.Model):
    img = models.ImageField(blank=True, null=True)
    place = models.ForeignKey(
            'Place', 
            related_name='images', 
            on_delete=models.CASCADE
        )
    order_num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.order_num}-{self.place.__str__()}'


class Place(models.Model):
    title = models.CharField(max_length=40)
    description_short = models.TextField(
        blank=True, 
        null=True
    )
    description_long = models.TextField()
    lon = models.DecimalField(
        null=True,
        max_digits=16,
        decimal_places=14,
        verbose_name='Longitude'
        )
    lat = models.DecimalField(
        null=True,
        max_digits=16,
        decimal_places=14,
        verbose_name='Latitude'
        )

    def __str__(self):
        return f'{self.title}'
