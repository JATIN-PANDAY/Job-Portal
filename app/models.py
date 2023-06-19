from django.db import models
# Create your models here.
import datetime


class UserMaster(models.Model):
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    otp=models.IntegerField()
    role=models.CharField(max_length=40)
    is_active=models.BooleanField(default=True)
    is_created=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False)
    is_updated=models.DateTimeField(auto_now_add=True)
 
class Candidate(models.Model):
    user_id= models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contact=models.IntegerField(max_length=10,null=True)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)

class Company(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    logo_pic=models.ImageField(upload_to='app/image/company',blank=True, null=True)


class jobpost(models.Model):
    company_id= models.ForeignKey(Company,on_delete=models.CASCADE)
    # if we get company_id we already get user_id
    jobname=models.CharField(max_length=50)
    companyname=models.CharField(max_length=50)
    companyaddress=models.CharField(max_length=50)
    jobdescreption=models.CharField(max_length=200)
    qualification=models.CharField(max_length=50)
    resposibilites=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    companyemail=models.CharField(max_length=200)
    companycontact=models.IntegerField(max_length=10)
    companywebsite=models.CharField(max_length=200)
    salarypackage=models.CharField(max_length=200)
    experience=models.CharField(max_length=50)
    date = models.DateField( default=datetime.date.today)
    logo_pic=models.ImageField(upload_to='app/image/jobpost')

# Job Apply 

class Applylist(models.Model):
    candidate= models.ForeignKey(Candidate,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    jobname=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    salaryexpected=models.CharField(max_length=50)
    resume=models.FileField(upload_to='app/resume')
    desc=models.CharField(max_length=200)    

class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40,null=True)
    subject=models.CharField(max_length=40)
    message=models.CharField(max_length=200,default=False)



