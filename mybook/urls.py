from django.urls import path
from mybook import views

urlpatterns=[
    path('',views.Home,name='homepage'),
    path('createAuthor',views.createAuthor,name='author'),
    path('createBook',views.CreateBook,name='book'),
]