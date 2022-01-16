from rest_framework import serializers
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .exceptions import DeletionError, InvalidInputError, RetrievalError, InvalidDataFound, EmptyResultSet
from .forms import ItemForm
import json


# from django.http import HttpResponse
from .models import Item
from .serializers import ItemSerializer
import uuid

# @api_view(['GET'])
# def get_items(request):
#     try:
#         all_items = Item.objects.filter(deletion_comment__isnull=True)
#         # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
#         serializer = ItemSerializer(all_items, many=True)

#         return JsonResponse(serializer.data, safe=False)
#     except:
#         return HttpResponse("There are no items in the inventory.")

# @api_view(['GET'])
# def get_deleted_items(request):
#     try:
#         deleted_items = Item.objects.filter(deletion_comment__isnull=False)
#         # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
#         serializer = ItemSerializer(deleted_items, many=True)

#         return JsonResponse(serializer.data, safe=False)
#     except:
#         return HttpResponse("There are no items in the inventory.")

# @api_view(['GET'])
# def get_item(request, item_id):
#     try:
#         curr_item = Item.objects.get(id=item_id)
#         # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
#         serializer = ItemSerializer(curr_item)
        
#         return JsonResponse(serializer.data, safe=False)
#     except:
#         # Exception occurs when item is not found.
#         return HttpResponse("Requested item does not exist.")

@api_view(['GET'])
def get_item(request, type):
    try:
        queryset = {}
        serializer = {}
        # check = {}
        if type == "all":
            print("You made it")
            queryset = Item.objects.filter(deletion_comment__isnull=True)
            # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
            serializer = ItemSerializer(queryset, many=True)

        elif type == "deleted":
            queryset = Item.objects.filter(deletion_comment__isnull=False)
            # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
            serializer = ItemSerializer(queryset, many=True)
        elif type.isnumeric():
            queryset = Item.objects.get(id=int(type))
            # Items are guaranteed to be serialized correctly. (error handling in creation/update workflows)
            serializer = ItemSerializer(queryset)
        else:
            raise RetrievalError()

        if queryset:
            return JsonResponse({"success": True, "message": "Item(s) retrieved!", "data": serializer.data})
        else:
            return EmptyResultSet()
        # # If there were no items found
        # if not queryset.exists():
        #     raise EmptyResultSet()
        # elif check.is_valid():
        #     return JsonResponse({"success": True, "message": "Item(s) retrieved!", "data": serializer.data})
        # # If retrieved data could not be serialized properly
        # # else:
        # #     raise InvalidDataFound()
        # item = None
        # serializer = {}

        # else:
            
        
        if item:
            return JsonResponse({"success": True, "message": "Item retrieved!", "data": serializer.data})


        


    except RetrievalError as retrieval_err:
        return JsonResponse({"success": False, "message": str(retrieval_err), "data": None})
    except EmptyResultSet as empty_res_err:
        return JsonResponse({"success": False, "message": str(empty_res_err), "data": None})
    except InvalidDataFound as invalid_data_found:
        return JsonResponse({"success": False, "message": str(invalid_data_found), "data": None})
    except Exception as e:
        print(e)
        # Exception occurs when item is not found.
        return JsonResponse({"success": False, "message": "Failed to update item due to unknown reasons. Please contact an administrator or try again later", "data": None})

@api_view(['POST'])
def post_item(request):
    try:
        data = JSONParser().parse(request)
        form = ItemForm(data)

        if form.is_valid():
            ## Maybe check to make sure same item name is not resused
            new_item = Item(uuid=uuid.uuid4(), name=data["name"], price=float(data["price"]), cogs=float(data["cogs"]), quantity=int(data["quantity"]), 
                origin_country=data["origin_country"], weight=float(data["weight"]))
            new_item.save()

            return JsonResponse({"success": True, "message": "Successfully created item!"})
        else:
            # Invalid data was inputted
            raise InvalidInputError()
        
    except InvalidInputError as invalid_inp_err:
        return JsonResponse({"success": False, "message": str(invalid_inp_err)})
    except:
        return JsonResponse({"success": False, "message": "Failed to update item due to unknown reasons. Please contact an administrator or try again later"})

@api_view(['PUT'])
def update_item(request, item_id):
    try:
        new_data = JSONParser().parse(request)
        curr_item = Item.objects.get(id = item_id)

        form = ItemForm(new_data)

        if form.is_valid():
            curr_item.name = new_data["name"]
            curr_item.price = new_data["price"]
            curr_item.cogs = new_data["cogs"]
            curr_item.quantity = new_data["quantity"]
            curr_item.origin_country = new_data["origin_country"]
            curr_item.weight = new_data["weight"]

            curr_item.save()
            return JsonResponse({"success": True, "message": f"Successfully updated item: {curr_item.name}"})
        else:
            # Invalid data was inputted
            raise InvalidInputError()
    except InvalidInputError as invalid_inp_err:
        return JsonResponse({"success": False, "message": str(invalid_inp_err)})
    except:
        print("hiya")
        return JsonResponse({"success": False, "message": "Failed to update item due to unknown reasons. Please contact an administrator or try again later"})


@api_view(['PUT'])
# Behind the scenes, this is a put request since it is updating an existing item
def soft_delete_item(request, item_id):
    try:
        data = JSONParser().parse(request)
        curr_item = Item.objects.get(id=item_id)

        # If item is already deleted, it can't be deleted again
        if curr_item.deletion_comment:
            raise DeletionError()

        # Calls Deletion model's delete method
        curr_item.delete(data["reason"])

        return JsonResponse({"success": True, "message": "Successfully deleted item!"})
    except DeletionError as deletion_err:
        return JsonResponse({"success": False, "message": str(deletion_err)})
    except: 
        return JsonResponse({"success": False, "message": "Failed to delete item due to unknown reasons. Please contact an administrator or try again later"})

        
@api_view(['DELETE'])
def hard_delete_item(request, item_id):
    try:
        Item.objects.delete(id=item_id)
        return HttpResponse("Success")
    except:
        return HttpResponse("Fail")
