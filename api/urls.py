from django.urls import path

from . import views

urlpatterns = [
    path('get/all', views.get_items, name="get_items"),
    path('get/<int:item_id>', views.get_item, name="get_item"),
    path('post/', views.post_item, name="post_item"),
    path('update/<int:item_id>', views.update_item, name="update_item"),
    # path('delete/<int:item_id>', views.delete_item, name="delete_item"),
]