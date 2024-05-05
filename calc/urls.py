from django.urls import path

from . import views
# you create this file and them add this in project url
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add')
]
 