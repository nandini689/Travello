from django.urls import path

from . import views
# you create this file and them add this in project url
urlpatterns = [
    path('',views.index,name='index')
]
 