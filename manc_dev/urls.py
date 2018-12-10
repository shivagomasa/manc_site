from django.urls import path
from . import views


urlpatterns = [

    path('',views.home_page,name='home_page'),

    path('about/',views.about, name='about'),

    path('careers/',views.careers,name='careers'),

    path('signup/',views.signup,name='signup'),
]