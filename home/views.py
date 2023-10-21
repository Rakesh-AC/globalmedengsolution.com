from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# Create your views here.


def home(request):
    user = request.user
    print("-=================")
    print(user.is_authenticated)
    print(type(user))
    print("-----------------------")
    if user.is_authenticated:
        print("TRUES: --------------")
        #check user is  job seeker or company
        try:
            #Checking if the user account as job seeker acount 
            job_seeker = JobSeekerAccount.objects.get(user = user)
            return render(request, "home/job_seeker_home.html")
        except:
            try: 
                # checking company_account 
                company_account = CompanyAccount.objects.get(user=user)
                return render(request, "home/company_home.html")
            except:
                #this means admin is logged in 
                print("Admin logged in")
                return redirect('/admin/')
    else:
        print("False: --------------")
        # user does not exists so  redirecting to generic template
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
            return redirect('/jobs/')
        else:
            messages.success(request, 'Invalid credentials, Please try again.')
            return redirect('/candidate-login/') 
            
    return render(request, "authentication/candidate_login.html")

def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/jobs/')
        else:
            messages.success(request, 'Invalid credentials, Please try again.')
            return redirect('/candidate-login/') 
    return render(request, "authentication/company_login.html")


from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages 
from . models import JobSeekerAccount, CompanyAccount

def candidate_signup(request):
    if request.method == "POST":

        print("---------------------------")
        print(request.POST)
        print("---------------------------")

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
        
        
        


        print("----------------   USER CREATED  ---------------------")

        
        
        
    return render(request, "authentication/candidate_signup.html")

def company_signup(request):

    return render(request, "authentication/company_signup.html")








def logout(request):
    logout(request)
    return redirect("/")

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
        

    print("DATA:   ",data)
    return JsonResponse(data)

