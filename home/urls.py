from home.views import BlogView
from django.urls import path

urlpatterns = [
    path('blog/', BlogView.as_view()),
    
]