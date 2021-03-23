
from django.contrib import admin
from django.urls import path
from .views import UserSignup,UserDetails,CustomerSupportView,ListCustomerSupportRequests,UserSignIn
urlpatterns = [
    path("SignUp",UserSignup.as_view()),
    path("signin",UserSignIn.as_view()),
    path("edit/<int:pk>",UserDetails.as_view()),
    path("support",CustomerSupportView.as_view()),
    path("list",ListCustomerSupportRequests.as_view()),
]
