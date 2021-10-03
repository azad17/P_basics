from django.urls import path
from . import views

app_name ='one'

urlpatterns = [
    path("",views.home,name="home"),
    path('add',views.add,name ="add"),
    path('list',views.BooksView.as_view(),name ='list'),
    path('details/<int:pk>/',views.BookDetails.as_view(),name='details'),
    path('update/<int:pk>/',views.BookUpdate.as_view(),name='update'),
    path('userset',views.BookData.as_view(),name='userset')
]