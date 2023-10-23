from django.db import models
from home.models import CompanyAccount
# Create your models here.

class Job(models.Model):
    # company = models.ForeignKey(CompanyAccount,null=True, blank=True,  on_delete=models.CASCADE)
    company = models.CharField(max_length=200, default="")
    job_name = models.CharField( max_length=200, default="")
    job_description = models.TextField( default="")
    salary = models.PositiveBigIntegerField()
    experience = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50, default="Any")
    job_location = models.CharField(max_length=200, default="")
    industry_type = models.CharField(max_length=200, default="")
    key_skills = models.CharField(max_length=500)
    posted_date = models.DateField( auto_now_add=True)
    number_of_openings = models.IntegerField()
    is_open = models.BooleanField(default=True)