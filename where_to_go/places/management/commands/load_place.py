import json
import requests

from django.core.management.base import BaseCommand

from django.core.files.base import ContentFile
from places.models import Image
from places.models import Place
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Load places from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='URL of JSON file')

    def print_success_message(self, place):
        msg = self.style.SUCCESS(f'Successfully loaded place "{place.title}"')
        self.stdout.write(msg)

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        item = json.loads(response.text)

        place, _ = Place.objects.get_or_create(
            title=item['title'],
            description_short=item['description_short'],
            description_long=item['description_long'],
            lon=float(item['coordinates']['lng']),
            lat=float(item['coordinates']['lat'])
        )

        for img_url in tqdm(item['imgs'], desc='Loading place'):
            response = requests.get(img_url)
            img_name = img_url.split('/')[-1]
            image = Image(place=place)
            image.img.save(img_name, ContentFile(response.content), save=True)
        self.print_success_message(place)
