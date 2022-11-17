from django.urls import path
from .views import (file_upload, user_posts, explore, user_profile,
                    delete_view, modify_post, post_view)

app_name = 'post'

urlpatterns = [
    path('post/', file_upload, name='user-post'),
    path('explore/', explore, name='explore'),
    path('user/', user_posts, name='user-file'),
    path('profile/<str:pk>/', user_profile, name='user-profile'),
    path('<id>/delete/', delete_view, name='post-delete'),
    path('<id>/modify/', modify_post, name='post-modify'),
    path('post_view/<str:pk>/', post_view, name='post-view'),

]