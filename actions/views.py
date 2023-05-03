from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .scraper import cgt_search, get_products_overview

# Create your views here.


@csrf_exempt
def save_product(request: HttpRequest) -> HttpResponse:
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


@csrf_exempt
def searching_from_CGT(request: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(request.body)['data']
        keywords = data['prompt']
        results = get_products_overview(keywords)
        return JsonResponse({'items': results})
    except Exception as e:
        return HttpResponse(str(e), status=500)
