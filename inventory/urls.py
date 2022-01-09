from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_main_page, name='index'),
    path('edit/<int:item_id>/', views.render_edit_page, name='render_edit_page'),
    path('edit/<int:item_id>/submit/', views.submit_edit, name="submit_edit"),
    path('edit/<int:item_id>/success/', views.render_edit_success, name="render_edit_success"),
    path('update/<int:item_id>/', views.update, name='update'),
]