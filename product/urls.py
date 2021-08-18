from . import views
from django.urls import path

urlpatterns = [
    path('fast-food-list/', views.ffList, name='fast-food-list'),
    path('fast-food-create/', views.ffCreate, name='fast-food-create'),
    path('fast-food-update/<int:id>', views.ffUpdate, name='fast-food-update'),
    path('fast-food-delete/<int:id>', views.ffDelete, name='fast-food-delete'),
]