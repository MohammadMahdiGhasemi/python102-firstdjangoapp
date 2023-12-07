from django.urls import path
from .views import posts , Home

urlpatterns = [
    path('',Home , name="home"),
    path("posts",posts,name="posts"),
]
    