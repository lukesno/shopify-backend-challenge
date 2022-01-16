from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from api.models import Deletion
from rest_framework.parsers import JSONParser 
from datetime import datetime

# from django.http import HttpResponse
# from .models import Item
import requests
import json
import uuid


def render_main_page(request):
    item_list = requests.get(f"http://127.0.0.1:8000/api/item/get/all")
    # Passing on response of item_list as a parameter to the html template
    context = json.loads(item_list.text)

    return render(request, 'inventory/index.html', context)

def render_deleted_page(request):
    deleted_items_list = requests.get(f"http://127.0.0.1:8000/api/item/get/deleted")
    context = json.loads(deleted_items_list.text)

    return render(request, 'inventory/deleted_items.html', context)

def render_create_page(request):
    return render(request, 'inventory/create/main.html')   

def render_edit_page(request, item_id):
    ## implement error checking?
    curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
    context = json.loads(curr_item.text)

    return render(request, 'inventory/edit/main.html', context)

def render_deletion_page(request, item_id):
    curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
    context = json.loads(curr_item.text)

    return render(request, 'inventory/delete/main.html', context)

@csrf_exempt
def submit_item(request):
    if request.method == 'POST':
        res = requests.post("http://127.0.0.1:8000/api/item/post/", data=json.dumps(request.POST))
        context = json.loads(res.text)

        return render(request, 'inventory/create/success.html', context)

@csrf_exempt
# POST request made from form
# Acts as an intermediate to call appropriate API calls before redirecting
def submit_edit(request, item_id):
    if request.method == 'POST':
        res = requests.put(f"http://127.0.0.1:8000/api/item/update/{item_id}", data=json.dumps(request.POST))
        context = json.loads(res.text)

        curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
        curr_item_json = json.loads(curr_item.text)

        context['data'] =  curr_item_json['data']

        return render(request, 'inventory/edit/success.html', context)

@csrf_exempt
def submit_deletion(request, item_id):
    if request.method == 'POST':
        res = requests.put(f"http://127.0.0.1:8000/api/item/delete/soft/{item_id}", data=json.dumps(request.POST))
        context = json.loads(res.text)

        return render(request, 'inventory/delete/success.html', context)


# @csrf_exempt
# def submit_hard_deletion(request, item_id):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)

#         if form.is_valid():
#             requests.post(f"http://127.0.0.1:8000/api/item/delete/{item_id}", data=json.dumps(request.POST))
#             return redirect(f"/delete/{item_id}/success")
#         else:
#             return HttpResponse("The information you inputted is invalid. Please try again.")




