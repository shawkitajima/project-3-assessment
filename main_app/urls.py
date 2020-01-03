from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wishes/create/', views.WishCreate.as_view(), name='wishes_create'),
    path('wishes/<int:wish_id>/delete/', views.wish_delete, name='wish_delete'),

]