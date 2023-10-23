from django.urls import path
from . import views
urlpatterns = [
    path("/", views.find_jobs, name="find_jobs"),
    path("my_jobs/", views.my_jobs, name="my_jobs"),
    
]
