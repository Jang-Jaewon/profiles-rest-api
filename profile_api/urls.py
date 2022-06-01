from django.urls import path
from profile_api import views


urlpatterns = [
    path('hello/', views.HelloAPIView.as_view()),
]