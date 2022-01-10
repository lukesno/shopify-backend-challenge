from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 

# from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
import requests
import json


def render_main_page(request):
    item_list = Item.objects.all()
    # Passing on item_list as a parameter to the html template
    context = {
        'item_list': item_list
    }

    return render(request, 'inventory/index.html', context)

def render_edit_page(request, item_id):
    ## implement error checking?
    curr_item = Item.objects.get(id = item_id)

    context = {
        'curr_item': curr_item
    }

    return render(request, 'inventory/edit/main.html', context)

def render_edit_success(request, item_id):
    ## implement error checking?
    curr_item = Item.objects.get(id = item_id)

    context = {
        'curr_item': curr_item
    }

    return render(request, 'inventory/edit/success.html', context)

@csrf_exempt
def submit_edit(request, item_id):
    # Check for validity of user input here

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            requests.put(f"http://127.0.0.1:8000/update/{item_id}/", data=json.dumps(request.POST))
            return redirect(f"/edit/{item_id}/success/")
        else:
            ## Create a template for this: user can go back to home page or try again
            return HttpResponse("The information you inputted is invalid. Please try again.")
    

@csrf_exempt
# PUT Request
# Updating a single item (identified by item_id) using the modifications passed into the request body
def update(request, item_id):
    new_data = JSONParser().parse(request)
    print(new_data)
    curr_item = Item.objects.get(id = item_id)

    curr_item.name = new_data["name"]
    curr_item.price = new_data["price"]
    curr_item.cogs = new_data["cogs"]
    curr_item.quantity = new_data["quantity"]
    curr_item.origin_country = new_data["origin_country"]
    curr_item.weight = new_data["weight"]

    curr_item.save()

    HttpResponse("Success!")
    



# def create(request):
# def delete(request):
# def get(request):




