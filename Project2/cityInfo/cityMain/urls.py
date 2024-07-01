from django.urls import path
from . import views

urlpatterns = [
    path('cityMain/', views.cityMain , name='cityMain'),
    path('cityNews/', views.cityNews , name='cityNews'),
    path('cityAdministration/', views.cityAdministration , name='cityAdministration'),
    path('cityFacts/', views.cityFacts , name='cityFacts'),
    path('cityContacts/', views.cityContacts , name='cityContacts')
   

]