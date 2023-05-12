# Generated by Django 4.2.1 on 2023-05-12 15:08

import json
import requests
from urllib.parse import urlparse, urlunparse, urljoin

from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.db import migrations
from tqdm import tqdm


def get_links():
    BASE_URL = "https://github.com/"
    url = "https://github.com/devmanorg/where-to-go-places/tree/master/places"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    all_links = soup.find_all("a", class_="js-navigation-open")
    links = []

    for link in all_links:
        href = link.get("href")
        if href.endswith(".json"):
            parsed = urlparse(href)
            path = parsed.path
            row_file_path = path.replace("blob", "raw")
            rel = urlunparse(parsed._replace(path=row_file_path))
            href = urljoin(BASE_URL, rel)
            links.append(href)
    return links


def handle(apps, schema_editor):
    Place = apps.get_model('places', 'Place')
    Image = apps.get_model('places', 'Image')
    urls = get_links()[:20]
    for json_url in tqdm(urls, desc='Loading places'):
        response = requests.get(json_url)
        response.raise_for_status()
        item = json.loads(response.text)

        place, _ = Place.objects.update_or_create(
            title=item['title'],
            description_short=item['description_short'],
            description_long=item['description_long'],
            lon=float(item['coordinates']['lng']),
            lat=float(item['coordinates']['lat'])
        )

        for img_url in item['imgs']:
            response = requests.get(img_url)
            img_name = img_url.split('/')[-1]
            image = Image(place=place)
            image.img.save(img_name, ContentFile(response.content), save=True)

    print('Successfully loaded places')


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20230507_1347'),
    ]

    operations = [
        migrations.RunPython(handle),
    ]
