from django.urls import path
from . import views

urlpatterns = [
    path('getData2/',views.getMethod,name='get2'),
    path('postData2/',views.postMethod,name='post2'),
    path('deleteData2/<int:id>/',views.deleteMethod,name='delete2'),
    path('updateData2/<int:id>/',views.updateMethod,name='update2'),
]