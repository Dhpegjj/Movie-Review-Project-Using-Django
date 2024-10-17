from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('movie/<int:movie_id>',views.detail,name='detail')
]