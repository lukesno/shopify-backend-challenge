from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_main_page, name='render_main_page'),
    path('deleted/', views.render_deleted_page, name='render_deleted_page'),
    path('edit/<int:item_id>/', views.render_edit_page, name='render_edit_page'),
    path('edit/<int:item_id>/submit/', views.submit_edit, name="submit_edit"),
    path('create/', views.render_create_page, name='render_create_page'),
    path('create/submit/', views.submit_item, name="submit_item"),
    path('remove/<int:item_id>/', views.render_deletion_page, name="render_deletion_page"),
    path('remove/<int:item_id>/submit/', views.submit_deletion, name="submit_deletion"),

    ## change these later
    path('remove/hard/<int:item_id>/submit/', views.submit_hard_deletion, name="submit_hard_deletion"),
    path('restore/<int:item_id>/submit/', views.submit_restoration, name="submit_restoration"),
]