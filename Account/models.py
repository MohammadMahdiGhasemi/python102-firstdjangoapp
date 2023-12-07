from django.db import models

class UserProfile(models.Model):
    first_name= models.CharField(max_length=50 , null=False , blank=True)
    company = models.CharField(max_length=50 , null=True)
    city = models.CharField(max_length=50 , null=True)
    last_name = models.CharField(max_length=50 , null=False , blank= True)
    job_title = models.CharField(max_length=50 , null=True)



