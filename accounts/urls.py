from accounts.views import RegisterView,LoginView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]