from django.urls import path

from user import views

urlpatterns = [
    path("register/", views.UserCreateView, name="register"),
    path("login/", views.UserLoginView, name="login"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]

app_name = "user"
