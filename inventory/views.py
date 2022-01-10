from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 

# from django.http import HttpResponse
# from .models import Item
from .forms import ItemForm
import requests
import json
import uuid


def render_main_page(request):
    item_list = requests.get(f"http://127.0.0.1:8000/api/item/get/all")
    # Passing on item_list as a parameter to the html template
    json_data = json.loads(item_list.text)

    context = { 'item_list': json_data }
    return render(request, 'inventory/index.html', context)

def render_edit_page(request, item_id):
    ## implement error checking?
    curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
    json_data = json.loads(curr_item.text)

    context = { 'curr_item': json_data }
    return render(request, 'inventory/edit/main.html', context)

def render_edit_success(request, item_id):
    ## implement error checking?
    curr_item = requests.get(f"http://127.0.0.1:8000/api/item/get/{item_id}")
    json_data = json.loads(curr_item.text)

    context = { 'curr_item': json_data }

    return render(request, 'inventory/edit/success.html', context)

def render_create_page(request):
    return render(request, 'inventory/create/main.html')

def render_create_success(request):
    return render(request, 'inventory/create/success.html')

@csrf_exempt
# POST request made from form, acts as intermediate to ensure valid data is passed onto update view
def submit_edit(request, item_id):
    # Check for validity of user input here

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # requests.get(f"http://127.0.0.1:8000/api/item/get/all")
            requests.put(f"http://127.0.0.1:8000/api/item/update/{item_id}", data=json.dumps(request.POST))
            return redirect(f"/edit/{item_id}/success/")
        else:
            ## Create a template for this: user can go back to home page or try again
            return HttpResponse("The information you inputted is invalid. Please try again.")

@csrf_exempt
def submit_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            requests.post("http://127.0.0.1:8000/api/item/post/", data=json.dumps(request.POST))
            return redirect("/create/success/")
        else:
            return HttpResponse("The information you inputted is invalid. Please try again.")
        




