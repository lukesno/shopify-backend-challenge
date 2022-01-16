from django.urls import path

from . import views

urlpatterns = [
    path('get/<str:type>', views.get_item, name="get_item"),
    path('post/', views.post_item, name="post_item"),
    path('update/<int:item_id>', views.update_item, name="update_item"),
    path('restore/<int:item_id>', views.restore_item, name="restore_item"),
    path('delete/soft/<int:item_id>', views.soft_delete_item, name="soft_delete_item"),
    path('delete/hard/<int:item_id>', views.hard_delete_item, name="hard_delete_item")
]