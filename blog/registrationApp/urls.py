from django.urls import path
from . import views

urlpatterns = [
    path('getData5/',views.getMethod,name='get5'),
    path('postData5/',views.postMethod,name='post5'),
    path('deleteData5/<int:id>/',views.deleteMethod,name='delete5'),
    path('updateData5/<int:id>/',views.updateMethod,name='update5'),
]