

from django.contrib import admin
from django.urls import path
from myapp.views import ItemListCreateView, ItemDetailView

urlpatterns= [
    path('api/items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('api/items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
      path('admin/', admin.site.urls),
]
