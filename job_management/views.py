from django.shortcuts import render

# Create your views here.


def find_jobs(request):
    return render(request, "job_management/find_jobs.html")



# for companies to display there jobs 
def my_jobs(request):
    if request.method == "POST":
        #add JOb object 
        pass
    return render(request, 'job_management/my_jobs.html')

#only for admin 
def all_jobs(request):
    return render(request, 'job_management/all_jobs.html')



