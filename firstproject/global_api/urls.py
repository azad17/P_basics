from django.urls import path
from global_api.api.v1 import views
urlpatterns =   [
    
    path('api/v1/fruit_list/',views.fruit_list,name = 'fruit_list'),
    path('api/v1/<int:pk>/',views.fruit_detail,name ='fruit_detail'),
    path('api/v1/users/',views.UserList.as_view(),name = 'UserList'),
    path('api/v1/fruits/',views.FruitsListView.as_view()),
    path('api/v1/fupdate/<int:pk>/',views.FruitsUpdateView.as_view())

]