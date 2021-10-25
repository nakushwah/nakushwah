from django.urls import path
from .views import CreateUser, RegisterView, LogInView, UpdateUser, LogoutView, VerifyEmail

urlpatterns = [
    # CRUD APIs
    path("ListCreateUser", CreateUser.as_view(), name="ListCreateUser"),
    path("UpdateUser/<pk>", UpdateUser.as_view(), name="UpdateUser"),
    # Auth APIs
    path('loginView/', LogInView.as_view(), name='LogIn'),
    path('LogoutView/', LogoutView.as_view(), name='Logout'),
    path("RegisterView/", RegisterView.as_view(), name="RegisterView"),
    path("VerifyEmail/<token>", VerifyEmail.as_view(), name="VerifyEmail"),

]
