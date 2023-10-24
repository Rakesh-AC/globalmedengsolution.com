from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request, "home/generic_home.html")
    
    

# Authentication Functions 

def candidate_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/')
        else:
            messages.warning(request, 'Invalid credentials, Please try again.')
            return redirect('/candidate-login/') 
    return render(request, "authentication/candidate_login.html")




from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages 
from . models import JobSeekerAccount, CompanyAccount

def candidate_signup(request):
    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=email, password=password)
        user.email=email
        user.first_name=first_name
        user.last_name = last_name
        user.save()

        job_seeker = JobSeekerAccount.objects.create(
                        user=user,
                        mobile_number = mobile_number
                    )
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials please try again")
            return HttpResponse('Something went wrong')
        
    return render(request, "authentication/candidate_signup.html")


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("/candidate-login/")


# Ajax validation functions -----------

#email validation AJAX
def validate_email(request):
    email = request.GET.get('email', None)
    data = { 'is_taken': False }
    try:
        user =User.objects.get(username=email)
        data = { 'is_taken': True }
    except:
        print("not found")
    return JsonResponse(data)



def view_profile(request):
    return render(request, 'profile_management/view_profile.html')



def contact_us(request):
    if request.method == "POST":
        print("---------------------")
        print(request.POST)
        print("---------------------")
        return render(request,"contact/contact_us.html")
    return render(request, "contact/contact_us.html")