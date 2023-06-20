from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

from products.models import Product
from products.serializers import ProductSerializer
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        
        data=serializer.data
    return Response(data)
    
    
    
    # instance= Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data=ProductSerializer(instance).data
    # return Response(data)
    
    
    
    # model_data= Product.objects.all().order_by("?").first()
    # data={}
    # if model_data:
    #     data=model_to_dict(model_data, fields=['id','title','price'])
    # return Response(data)

    # model_data= Product.objects.all().order_by("?").first()
    # data={}
    # if model_data:
    #     data=model_to_dict(model_data, fields=['id','title'])
    # return JsonResponse(data)
    
        # body=request.body #byte string of JSON Data
    # data={}
    # try:
    #     data=json.loads(body)
    # except:
    #     pass
    # data['params']=dict(request.GET)
    # data['headers']=dict(request.headers)
    # data['content_type']=request.content_type
