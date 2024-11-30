from django.urls import path, include
from . import views
urlpatterns = [
    # path('register/', views.register, name='register'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('edit/', views.edit_profile, name = "edit_profile"),
    path('pass_change/', views.pass_Change, name = "pass_change"),
]
