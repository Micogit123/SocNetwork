from django.urls import path
from . import views
from django.contrib.auth.views import (login, logout, password_reset, password_reset_done,
     password_reset_confirm, password_reset_complete)


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('', login, {'template_name': 'polls/home.html'}),
    path('logout/', logout, {'template_name': 'polls/home.html'}),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name="profile_edit"),
    path('change-password/', views.change_password, name="change_password"),
    path('reset-password/', password_reset, name="reset_password"),
    path('reset-password/done/', password_reset_done, name="password_reset_done"),
    path('reset-password/confirm/(?P<uidb64> [0-9A-Za-z]+)-(?P<token>.+)', password_reset_confirm, 
    	name="password_reset_confirm"),
    path('reset-password/complete/', password_reset_complete, name="password_reset_complete"),
    path('other_profiles/', views.other_profiles, name="other_profiles"),
    path('delete_profile/', views.delete_profile, name="delete_profile"),
    path('cities/', views.cities, name="cities"),
    path('friendlist/', views.friendlist, name="friendlist"),
    path('search_users/', views.search_users, name="search_users"),
]
