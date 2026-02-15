from django.urls import path
from . import views

urlpatterns = [
    path('getData4/', views.getMethod, name='get4'),
    path('postData4/', views.postMethod, name='post4'),
    path('deleteData4/<int:id>/', views.deleteMethod, name='delete4'),
    path('updateData4/<int:id>/', views.updateMethod, name='update4'),
]