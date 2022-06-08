from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profile_api import views


router = DefaultRouter()
router.register("hello-test", views.HelloViewSet, basename="hello-test")
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeedViewset)

urlpatterns = [
    path('hello/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]
