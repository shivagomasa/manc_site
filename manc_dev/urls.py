from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('',views.home_page,name='home_page'),

    path('about/',views.about, name='about'),

    path('careers/',views.careers,name='careers'),

    path('login/',LoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(),name='logout'),

    path('signup/',views.signup, name='signup'),

    path('account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

    path('contact/',views.contact,name='contact'),

    path('contact/thanks/',views.thanks,name='thanks'),
]