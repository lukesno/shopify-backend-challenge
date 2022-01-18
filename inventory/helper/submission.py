from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from api.models import Deletion
from rest_framework.parsers import JSONParser 
from datetime import datetime

import requests
import json
import uuid

# "submission_handler" view in views.py call these functions
# Contains helper functions to render appropriate pages

# Handles form submission in create page
# Calls the post_item API in "api/views.py" then navigates to a result template page
def submit_item(request):
    if request.method == 'POST':
        res = requests.post("http://127.0.0.1:8000/api/item/post/", data=json.dumps(request.POST))
        context = json.loads(res.text)

        return render(request, 'inventory/result.html', context)

# Handles form submission in edit page
# Calls the update_item API in "api/views.py" then navigates to a result template page
def submit_edit(request, item_id):
    if request.method == 'POST':
        res = requests.put(f"http://127.0.0.1:8000/api/item/update/{item_id}", data=json.dumps(request.POST))
        context = json.loads(res.text)

        curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
        curr_item_json = json.loads(curr_item.text)

        context['data'] =  curr_item_json['data']

        return render(request, 'inventory/result.html', context)

# Handles the deletion reason that is passed on from the deletion page
# Soft deletes the item by calling the "soft_delete_item" API
def submit_soft_deletion(request, item_id):
    if request.method == 'POST':
        res = requests.put(f"http://127.0.0.1:8000/api/item/delete/soft/{item_id}", data=json.dumps(request.POST))
        context = json.loads(res.text)

        return render(request, 'inventory/result.html', context)

# Handles the "Delete Permanently" action from deleted items page
# Hard deletes the item by calling the "hard_delete_item" API
def submit_hard_deletion(request, item_id):
    res = requests.delete(f"http://127.0.0.1:8000/api/item/delete/hard/{item_id}")
    context = json.loads(res.text)

    return render(request, 'inventory/result.html', context)

# Handles "Restore Item" action from deleted items page
# Restores the item by calling the "restore_item" API
def submit_restoration(request, item_id):
    res = requests.put(f"http://127.0.0.1:8000/api/item/restore/{item_id}")
    context = json.loads(res.text)

    # replace the template with the general one
    return render(request, 'inventory/result.html', context)





