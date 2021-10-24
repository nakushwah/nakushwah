from django.urls import path
from .views import CreateUser, RegisterView, LogInView, UpdateUser,LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # CRUD APIs
    path("ListCreateUser", CreateUser.as_view(), name="ListCreateUser"),
    path("UpdateUser/<pk>", UpdateUser.as_view(), name="UpdateUser"),

    # Auth APIs
    path('loginView/', LogInView.as_view(), name='LogIn'),
    path('LogoutView/', LogoutView.as_view(), name='Logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("RegisterView/", RegisterView.as_view(), name="RegisterView"),

]
