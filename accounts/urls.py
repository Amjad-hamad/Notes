from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path('login',views.login , name='login'),
    path('signup',views.signup , name='signup'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    
]
