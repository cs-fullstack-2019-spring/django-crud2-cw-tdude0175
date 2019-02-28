from django.urls import path

from . import views

urlpatterns = \
    [
        # each path leads to it's own page with various links between each
        path('', views.index , name = 'index'),
        path('newUser/', views.createUser, name = 'createUser'),
        path('deleteUser/<int:userID>/', views.deleteUser, name ='deleteUser'),
        path('updateUser/<int:userID>/', views.updateUser, name ='updateUser'),
    ]