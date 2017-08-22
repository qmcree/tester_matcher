from django.http import JsonResponse, HttpResponseNotAllowed, HttpRequest

from .models import Country, Device

response_not_allowed = HttpResponseNotAllowed(('GET',))


def list_options(request):
    if request.method != 'GET':
        return response_not_allowed

    country_queryset = list(Country.objects.all())
    device_queryset = list(Device.objects.all())

    countries = [
        {'code_iso2': country.code_iso2, 'name': country.name} for country in country_queryset
    ]
    devices = [
        {'id': device.pk, 'name': device.name} for device in device_queryset
    ]

    return JsonResponse({
        'countries': countries,
        'devices': devices,
    }, safe=False)


def list_testers(request: HttpRequest):
    if request.method != 'GET':
        return response_not_allowed
