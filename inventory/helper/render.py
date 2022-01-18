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


# "router" view in views.py call these functions
# Contains helper functions to render appropriate pages

# Helper function that renders main page
# Calls custom "get_item" API in api/views.py
def render_main_page(request):
    item_list = requests.get(f"http://127.0.0.1:8000/api/item/get/all")
    # Passing on response of item_list as a parameter to the html template
    context = json.loads(item_list.text)

    return render(request, 'inventory/index.html', context)

# Helper function that renders a page with all items that were deleted by any users
# Calls custom "get_item" API in api/views.py
def render_deleted_page(request):
    deleted_items_list = requests.get(f"http://127.0.0.1:8000/api/item/get/deleted")
    context = json.loads(deleted_items_list.text)

    return render(request, 'inventory/deleted_items.html', context)

# Helper function that renders a page where users can edit existing items
# Calls custom "get_item" API in api/views.py
def render_edit_page(request, item_id):
    ## implement error checking?
    curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
    context = json.loads(curr_item.text)

    return render(request, 'inventory/edit/main.html', context)

# Helper function that renders a page where users can edit existing items
# Calls custom "get_item" API in api/views.py
def render_deletion_page(request, item_id):
    curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
    context = json.loads(curr_item.text)

    return render(request, 'inventory/delete/soft/main.html', context)


# Helper function that renders a page where users can create new items
def render_create_page(request):
    return render(request, 'inventory/create/main.html')   