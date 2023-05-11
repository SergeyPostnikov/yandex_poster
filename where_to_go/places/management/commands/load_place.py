import json
import requests

from django.core.management.base import BaseCommand

from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Load places from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='URL of JSON file')

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        item = json.loads(response.text)

        place = Place.objects.create(
            title=item['title'],
            description_short=item['description_short'],
            description_long=item['description_long'],
            lon=item['coordinates']['lng'],
            lat=item['coordinates']['lat']
        )

        for img_url in item['imgs']:
            response = requests.get(img_url)
            img_name = img_url.split('/')[-1]
            image = Image(place=place)
            image.img.save(img_name, ContentFile(response.content), save=True)

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded place "{place.title}"'))
