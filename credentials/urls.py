from django.urls import path

from . import views
# you create this file and them add this in project url
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]