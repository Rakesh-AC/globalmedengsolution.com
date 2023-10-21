from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CompanyAccount(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True )


class JobSeekerAccount(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=100)
    jobs_applied = models.ManyToManyField("job_management.Job", blank=True)











