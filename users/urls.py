from django.urls import path, re_path
from . import views
# from rest_framework_simplejwt import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/login/", views.UserLoginView.as_view()),
    # path("token/", views.TokenObtainPairView.as_view()),
    # path("token/refresh/", views.TokenRefreshView.as_view()),
]
