from rest_framework import serializers
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import json

# from django.http import HttpResponse
from .models import Item
from .serializers import ItemSerializer
import uuid

@api_view(['GET'])
def get_items(request):
    try:
        all_items = Item.objects.all()
        # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
        serializer = ItemSerializer(all_items, many=True)

        return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse("There are no items in the inventory.")

@api_view(['GET'])
def get_item(request, item_id):
    try:
        curr_item = Item.objects.get(id=item_id)
        # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
        serializer = ItemSerializer(curr_item)
        
        return JsonResponse(serializer.data, safe=False)
    except:
        # Exception occurs when item is not found.
        return HttpResponse("Requested item does not exist.")

@api_view(['POST'])
def post_item(request):
    try:
        data = JSONParser().parse(request)

        ## Maybe check to make sure same item name is not resused
        new_item = Item(uuid=uuid.uuid4(), name=data["name"], price=float(data["price"]), cogs=float(data["cogs"]), quantity=int(data["quantity"]), 
            origin_country=data["origin_country"], weight=float(data["weight"]))
        new_item.save()
        
        return HttpResponse("Success")
    except:
        return HttpResponse("Fail")

@api_view(['PUT'])
def update_item(request, item_id):
    try:
        new_data = JSONParser().parse(request)
        curr_item = Item.objects.get(id = item_id)

        curr_item.name = new_data["name"]
        curr_item.price = new_data["price"]
        curr_item.cogs = new_data["cogs"]
        curr_item.quantity = new_data["quantity"]
        curr_item.origin_country = new_data["origin_country"]
        curr_item.weight = new_data["weight"]

        curr_item.save()

        return HttpResponse("Success")
    except:
        return HttpResponse("Fail")


# @api_view(['DELETE'])
# def delete_item(request, item_id):