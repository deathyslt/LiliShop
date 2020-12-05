from django.urls import path, include

from .views import show_all_stores, show_store_flowers

urlpatterns = [
    path('show_all_stores',
         show_all_stores, name='show-all-stores'),
    path('store/<str:store_name>', show_store_flowers, name='show_store_flowers'),
]
