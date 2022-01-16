from django.urls import path

from . import views

urlpatterns = [
    # path('get/all', views.get_items, name="get_items"),
    # path('get/deleted', views.get_deleted_items, name="get_deleted_items"),
    # path('get/<int:item_id>', views.get_item, name="get_item"),
    path('get/<str:type>', views.get_item, name="get_item"),
    path('post/', views.post_item, name="post_item"),
    path('update/<int:item_id>', views.update_item, name="update_item"),
    path('delete/soft/<int:item_id>', views.soft_delete_item, name="soft_delete_item"),
    path('delete/hard/<int:item_id>', views.hard_delete_item, name="hard_delete_item")
]