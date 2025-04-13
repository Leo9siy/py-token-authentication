from django.urls import path

from user import views

urlpatterns = [
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]

app_name = "user"
