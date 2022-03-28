from django.urls import path
from . import views

urlpatterns=[
    path('',views.fnh,name=""),
    path('admindashboard/',views.fnaddash,name="admindashboard"),
    path('booking/',views.fnadbook,name="booking"),
    path('rooms/',views.fnadrooms,name="rooms")
]
