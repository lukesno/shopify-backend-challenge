from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Importing helper functions for "router" function
from .helper.render import render_main_page, render_deleted_page, render_create_page, render_deletion_page, render_edit_page
from .helper.submission import submit_item, submit_soft_deletion, submit_edit, submit_hard_deletion, submit_restoration

# Overrides default 404 handler to render reroute page.
def invalid_url_handler(request, exception):
    return render(request, 'inventory/invalid_url.html')

# Renders appropriate template page according to url accessed.
# Utilizes helper functions in helper/render.py
def router(request, *args, **kwargs):
    url_type = kwargs.get("url_type")
    item_id = kwargs.get("item_id", None)

    if url_type == "main":
        return render_main_page(request)
    elif url_type == "deleted":
        return render_deleted_page(request)
    elif url_type == "create":
        return render_create_page(request)
    elif url_type == "remove":
        return render_deletion_page(request, item_id)
    elif url_type == "edit":
        return render_edit_page(request, item_id)
    else:
        return render(request, 'inventory/invalid_url.html')


# Handles actions that require data handling from every sub page (edit, create, delete)
# Calls helper functions to handle access to APIs for each case
@csrf_exempt
def submission_handler(request, *args, **kwargs):
    url_type = kwargs.get("url_type")
    item_id = kwargs.get("item_id", None)

    if url_type == "create":
        return submit_item(request)
    elif url_type == "edit":
        return submit_edit(request, item_id)
    elif url_type == "remove":
        return submit_soft_deletion(request, item_id)
    elif url_type == "annihilate":
        return submit_hard_deletion(request, item_id)
    elif url_type == "restore":
        return submit_restoration(request, item_id)
    else:
        return render(request, 'inventory/invalid_url.html')

