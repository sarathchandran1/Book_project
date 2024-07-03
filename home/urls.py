
from django.urls import path
from . import views
urlpatterns = [
  path('createbook/',views.createBook,name='createbook'),
  path('createauther/',views.Create_Auther,name='auther'),
  path('',views.list_book,name='booklist'),
  path('deatilesview/<int:book_id>/',views.deatiles_View,name='details'),
  path('updateview/<int:book_id>/',views.updateBook,name='update'),
  path('deleteview/<int:book_id>/',views.deleteView,name='delete'),
  path('base/',views.index),
  path('search/',views.search_book,name='search')
]