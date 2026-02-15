from django.urls import path
from . import views


urlpatterns = [
    path('getData1/', views.getMethod, name='get1'),
    path('postData1/', views.postMethod, name='post1'),
    path('delData1/<int:id>/', views.deleteMethod, name='del1'),
    path('updateData1/<int:id>/', views.updateMethod, name='update1'),
]