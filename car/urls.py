from django.urls import path, include
from . import views
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('details/<int:id>/', views.DetailCarView.as_view(), name="detail_car"),
    path('buy/<int:car_id>/', views.buy_now, name="buy_now"),  # New URL for buying cars
    
]
