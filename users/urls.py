from django.urls import path
from .views import home, RegisterView, profile


app_name = 'users'

urlpatterns = [
    path('', home, name='users-home'),
    path('users/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile')

]