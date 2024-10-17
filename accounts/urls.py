from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/',views.signupaccount,name='signupaccount'),
    path('loginaccount/',views.loginaccount,name='loginaccount'),
    path('logout/',views.logoutaccount,name='logoutaccount')
]
