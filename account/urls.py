from django.urls import path
from . import views
urlpatterns = [
 path('register/',views.reister_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home')

]