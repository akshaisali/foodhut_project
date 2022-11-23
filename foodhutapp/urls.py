from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'foodhutapp'


urlpatterns = [
     path("", views.index, name="index"),
     path('signup/',views.signup, name='signup'),
     path('login/',views.login, name='login'),
     
     path('login/salad/',views.salad, name='salad'),
     path('login/pizza/',views.pizza, name='pizza'),
     path('login/burger',views.burger, name='burger'),
     path('login/dessert/',views.dessert, name='dessert'),
     path('login/drinks/',views.drinks, name='drinks'),
     path('login/seafood/',views.seafood, name='seafood'),
     
]
