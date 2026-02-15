from django.urls import path
from . import views

urlpatterns = [
    path('getData3/',views.getMethod,name='get3'),
    path('postData3/',views.postMethod,name='post3'),
    path('deleteData3/<int:id>/',views.deleteMethod,name='delete3'),
    path('updateData3/<int:id>/',views.updateMethod,name='update3'),
]