from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


@csrf_exempt
def my_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)['data']

        return HttpResponse('Post request detected')
    else:
        return HttpResponseNotFound('This is a GET request')


@csrf_exempt
def get_product_photos(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        # data = request.body.decode('utf-8')
        data = json.loads(request.body)
        print(data, type(data))
        return HttpResponse('Post request detected')
    else:
        return HttpResponse('This is a GET request')
