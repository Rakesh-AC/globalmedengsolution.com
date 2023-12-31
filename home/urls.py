from django.urls import path 
from . import views

urlpatterns = [
    path('',  views.home, name="homepage"),

    # Authentication Functions 
    path('candidate-login/', views.candidate_login, name="candidate_login" ),
    path('candidate-signup/', views.candidate_signup, name="candidate_signup" ),
    # path('company-login/', views.company_login, name="company_login" ),
    # path('company-signup/', views.company_signup, name="company_signup" ),

    #log out function 
    path("log-out/", views.logout_user, name="logout"),

    #validation functions 
    path('validate_email/', views.validate_email, name="validate_email"), 

    #profile
    path('view-profile/', views.view_profile, name="view_profile"),

    #contact us page
    path('contact-us/', views.contact_us, name="contact_us"),

]
