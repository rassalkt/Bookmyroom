from django.urls import path
from . import views

urlpatterns=[
    path('master',views.fnmaster,name="master"),
    path('',views.fnhome,name="home"),
    path('aboutus/',views.fnabtus,name="aboutus"),
    path('stays/',views.fnstays,name="stays"),
    path('calicut/',views.fncalicut,name="calicut")
]