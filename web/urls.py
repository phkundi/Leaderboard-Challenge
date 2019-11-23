from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('leaderboard/', views.ranking, name="ranking"),
    path('privacy_policy/', views.PrivacyView.as_view(), name="privacy"),
    path('checkout/', views.payment_view, name="payment"),
]