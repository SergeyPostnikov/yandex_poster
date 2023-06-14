from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from places.models import Place


def get_place(request, pk) -> JsonResponse:
    place_queryset = Place.objects.prefetch_related('images')
    place = get_object_or_404(place_queryset, pk=pk)
    return JsonResponse(
        data={
            "title": place.title,
            "imgs": [image.img.url for image in place.images.all()],
            "short_description": place.short_description,
            "long_description": place.long_description,
            "coordinates": {
                "lat": place.lat,
                "lng": place.lon
            }
        },
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )


def serialize_places(places):
    geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "detailsUrl": reverse(get_place, kwargs={'pk': place.pk})
            },
        }
        geojson['features'].append(feature)
    return geojson


def index(request):
    all_places = Place.objects.all()
    geojson = serialize_places(all_places)
    return render(request, 'index.html', context={'geojson': geojson})
