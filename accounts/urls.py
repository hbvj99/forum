from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.dashboard, name='profile'),
    path('profile/change/', views.image_update, name='image_update'),
    path('edit/', views.edit_account, name='edit_account'),
]