from django.urls import path
from . import views
urlpatterns = [
  path('user/',views.list_book,name='booklist'),
  path('userdeatiles/<int:book_id>/',views.deatiles_View,name='details'),
  path('user_search/',views.search_book,name='usersearch'),
  path('addtocart/<int:book_id>',views.Add_to_cart,name='addtocart'),
  path('viewcart/',views.ViewCart,name='viewcart'),
  path('increase/<int:item_id>',views.increase_quantity,name='increase_quantity'),
  path('decrease/<int:item_id>',views.decrease_quantity,name='decrease_quantity'),
  path('removecart/<int:item_id>',views.remove_from_cart,name='remove_cart'),
  path('createcheckout/',views.create_checkout_session,name='checkout'),
  path('success/',views.success,name='success'),
  path('cancel/',views.cancel,name='cancel')
]