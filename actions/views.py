from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .scraper import cgt_search, get_products_overview, get_product_info
from photos.serializers import AddImageSerializer
# Create your views here.


@csrf_exempt
def save_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)['data']
        product_info = get_product_info(
            url=data['url'], collection=data['collection'])

        if product_info is not None:
            serializer = AddImageSerializer(data=product_info)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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


@csrf_exempt
def searching_from_CGT(request: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(request.body)['data']
        keywords = data['prompt']
        results = get_products_overview(keywords)
        return JsonResponse({'items': results})
    except Exception as e:
        return HttpResponse(str(e), status=500)
