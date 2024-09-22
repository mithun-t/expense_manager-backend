from django.urls import path
from .views import CategoryMaster, ExpenseMaster

urlpatterns = [
    path('categories/', CategoryMaster.as_view(), name='category-list'),
    path('expenses/', ExpenseMaster.as_view(), name='expense-list'),
]
