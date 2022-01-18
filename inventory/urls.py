from django.urls import path
from django.views.generic import RedirectView

from . import views

# All base urls call a general router view, which renders template pages accordingly.
# Similarily, all submission urls call a general submission view, which calls intermediate functions to handle API requests
urlpatterns = [
    # Redirects default url to main page
    path('', RedirectView.as_view(url='/main/'), name='main'),
    path('<str:url_type>/', views.router, name='router'),
    path('<str:url_type>/<int:item_id>/', views.router, name='router'),
    path('<str:url_type>/submit/', views.submission_handler, name='submission_handler'),
    path('<str:url_type>/<int:item_id>/submit/', views.submission_handler, name='submission_handler'),
    
]